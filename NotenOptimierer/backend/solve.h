#ifndef SOLVE_H
#define SOLVE_H

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <utility>
#include <tuple>
#include <algorithm>
#include <queue>
#include <string>

using namespace std;

typedef struct GradePair {
	double grade,credits;
	string subjectId;

	GradePair(double g, double c, string sid) : grade(g), credits(c), subjectId(sid) {}

	GradePair addGradePair(const GradePair gp) const {
		double sum_gradePoints = grade*credits + gp.grade*gp.credits;
		double sum_credits = credits + gp.credits;
		return GradePair(sum_gradePoints/sum_credits, sum_credits, subjectId);
	} 

	GradePair addGradePair(const double g, const double c) const {
		double sum_gradePoints = grade*credits + g*c;
		double sum_credits = credits + c;
		return GradePair(sum_gradePoints/sum_credits, sum_credits, subjectId);
	} 

	GradePair subGradePair(const GradePair gp) const {
		double sum_gradePoints = grade*credits - gp.grade*gp.credits;
		double sum_credits = credits - gp.credits;
		return GradePair(sum_gradePoints/sum_credits, sum_credits, subjectId);
	}

	GradePair subGradePair(const double g, const double c) const {
		double sum_gradePoints = grade*credits - g*c;
		double sum_credits = credits - c;
		return GradePair(sum_gradePoints/sum_credits, sum_credits, subjectId);
	} 
} GradePair;


ostream& operator<< (ostream& os, const GradePair& gp) {
	os << gp.grade << "," << gp.credits << "," << gp.subjectId;
	return os;
}

bool operator<(const GradePair& gp1, const GradePair& gp2) {
	return (gp1.grade < gp2.grade);
}


typedef struct Node {
	vector<int> deletions;
	GradePair gradepair;
	double remCred;

	Node(vector<int> d, GradePair g, double rc) : deletions(d), gradepair(g), remCred(rc) {}

	int level() const {
		return deletions.size();
	}
} Node;

ostream& operator<< (ostream& os, const Node& n) {
	os << "{[";
	for(int del : n.deletions) {
		os << del << ", ";
	}
	os << "], " << n.gradepair << ", " << n.remCred << "}";
	return os;
}

GradePair parseGrade(string pair);

vector<string> split(string toSplit, char delimeter);

vector<vector<GradePair>> parseFile(char *filename);

void printGrades(vector<vector<GradePair>> grades);

vector<GradePair> solve(vector<vector<GradePair>> input);

double calcUB(const Node n, const vector<vector<GradePair>> input, const vector<GradePair>& sectionGrades);

double calcLB(const Node n, const vector<vector<GradePair>> input, const vector<GradePair>& sectionGrades);

#endif
