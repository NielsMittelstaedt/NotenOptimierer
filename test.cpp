#include "test.h"


GradePair parseGrade(string pair) {
	vector<string> splitPair = split(pair, ',');
	return GradePair(atof(splitPair[0].c_str()), atof(splitPair[1].c_str()));
}

vector<string> split(string toSplit, char delimeter) {
	std::stringstream ss(toSplit);
	string item;
	vector<string> result;
	while(std::getline(ss, item, delimeter)) {
		result.push_back(item);
	}
	return result;
}

vector<vector<GradePair>> parseFile(char *filename) {
	std::ifstream infile(filename);
	string line;
	std::getline(infile, line);
	vector<vector<GradePair>> result;
	while(std::getline(infile, line)) {
		vector<string> splitLine = split(line, ';');
		vector<GradePair> section;
		for(string pair : splitLine) {
			section.push_back(parseGrade(pair));
		}
		result.push_back(section);
	}
	return result;
}

void printGrades(vector<vector<GradePair>> grades) {
	cout << "{\n";
	for(auto section : grades) {
		cout << "\t{\n";
		for(auto pair : section) {
			cout << "\t\t" << pair.grade << "," << pair.credits << "\n";
		}
		cout << "\t}\n";
	}
	cout << "}\n";
}

vector<GradePair> solve(vector<vector<GradePair>> input, double deletableCredits) {
	//Sort the grades in each section in descending order
	
	for(vector<GradePair> &section : input) {
		sort(section.begin(), section.end());
	}
	

	//Calculate grades for every section, if no grade was deleted
	vector<GradePair> sectionGrades;
	for(vector<GradePair> section : input) {
		double gradePoints = 0;
		double credits = 0;
		for(GradePair pair : section) {
			gradePoints += pair.credits*pair.grade;
			credits += pair.credits;
		}
		sectionGrades.push_back(GradePair(gradePoints/credits, credits));
	}

	//Branch and Bound
	queue<Node> activeNodes;
	activeNodes.push(Node(vector<int>{-1}, input[0][0], deletableCredits));

	double bestUB = 4.0;
	Node bestNode(vector<int>{}, GradePair(4, 0), 10000000);


	while(!activeNodes.empty()) {
		Node n = activeNodes.front();
		activeNodes.pop();
		//cout << n << "\n";

		if(n.level() == input.size()) {
			if(n.gradepair.grade <= bestNode.gradepair.grade)
				bestNode = n;
		}
		else {
			vector<int> nextDeletions = n.deletions;
			nextDeletions.push_back(-1);

			//Case where no other grade is deleted
			Node deleteNone(nextDeletions, n.gradepair.addGradePair(sectionGrades[n.level()]), n.remCred);
			activeNodes.push(deleteNone);

			for(int i = 0; i < input[n.level()].size(); ++i) {
				if(input[n.level()][i].credits <= n.remCred) {
					nextDeletions[nextDeletions.size()-1] = i;
					GradePair gp = input[n.level()][i];
					Node deleteNext(nextDeletions, n.gradepair.addGradePair(sectionGrades[n.level()].subGradePair(gp)), n.remCred-gp.credits);
					activeNodes.push(deleteNext);
				}
			}
		}
	}

	vector<GradePair> gradesToDelete;
	for(int i = 0; i < input.size(); ++i) {
		if(bestNode.deletions[i] == -1) {
			gradesToDelete.push_back(GradePair(0, 0));
		} else {
			gradesToDelete.push_back(input[i][bestNode.deletions[i]]);
		}
	}

	return gradesToDelete;
}

double calcUB(const Node& n, const vector<vector<GradePair>>& input, const vector<GradePair>& sectionGrades) {
	if(n.level() == input.size()) return n.gradepair.grade;
	double cr_remain = n.remCred;

	GradePair totalGrade = n.gradepair;

	for(int i = n.level(); i < input.size(); ++i) {
		auto worst = input[i][0];
		if(worst.credits <= cr_remain) {
			cr_remain -= worst.credits;
			totalGrade = totalGrade.addGradePair(worst);
		}
	}

	return totalGrade.grade;
}

double calcLB(const Node n, const vector<vector<GradePair>> input, const vector<GradePair>& sectionGrades) {
	if(n.level() == input.size()) return n.gradepair.grade;
	return 0;
}

int main(int argc, char *argv[]) {
	if(argc != 2) {
		cout << "Filename required" << std::endl;
		return 0;
	}
	char* filename = argv[1];
	std::ifstream infile(filename);
	string controlline;
	std::getline(infile, controlline);
	double deletableCredits = atof(controlline.c_str());

	vector<vector<GradePair>> grades = parseFile(argv[1]);
	vector<GradePair> result = solve(grades, deletableCredits);
	for(auto gp : result) {
		std::cout << gp.grade << "," << gp.credits << "\n";
	}
	
	return 0;
}


