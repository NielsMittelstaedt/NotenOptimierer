class Solver:
    def __init__(self, input, thesis):
        # array of array of tuple
        #input = [[(2.7,8),(3,8),(2.7,6),(3,6)], [(1.7,6),(2.3,6),(3.3,6)], [(4,6),(4,7),(4,7)], [(3.7,6),(4,6),(3.3,8),(3.3,6)]]
        input = [[(1.3,8),(1,8),(1.7,6),(1,6)],[(1,6),(1.3,6),(1.3,6)],[(1,6),(1.7,7),(1.7,7)],[(3,6),(2.3,6),(1,8),(1,6)],[(1,3),(1,5)],[(1.7,6),(1.7,6),(1,6),(1.7,6)],[(1,6),(1,6),(1,6),(2,4)]]

        input_sorted = []

        for section in input:
            input_sorted.append(sorted(section, key=lambda x: x[0], reverse=True))

        self.input = input_sorted
        self.thesis = thesis

    def calc_lb(self, node):
        (del_nodes, grade, credit_sum, remaining_credits) = node
        section_index = len(del_nodes)

        deletions = []

        sum_grades = grade*credit_sum
        sum_credits = credit_sum

        for i in range(section_index, len(self.input)):
            worst = self.input[i][0][0]

            for j in range(len(self.input[i])):
                if self.input[i][j][0] < worst:
                    sum_grades += self.input[i][j][0]*self.input[i][j][1]
                    sum_credits += self.input[i][j][1]
                elif worst < grade:
                    sum_grades += self.input[i][j][0]*self.input[i][j][1]
                    sum_credits += self.input[i][j][1]

        return sum_grades/sum_credits

    def calc_ub(self, node):
        (del_nodes, grade, credit_sum, remaining_credits) = node
        section_index = len(del_nodes)

        deletions = []

        for i in range(section_index, len(self.input)):
            if self.input[i][0][0] >= grade and self.input[i][0][1] <= remaining_credits:
                remaining_credits -= self.input[i][0][1]
                deletions.append(True)
            else:
                deletions.append(False)
        
        sum_grades = grade*credit_sum
        sum_credits = credit_sum

        for i in range(section_index, len(self.input)):
            if not deletions.pop(0):
                sum_grades += self.input[i][0][0]*self.input[i][0][1]
                sum_credits += self.input[i][0][1]

            for j in range(1, len(self.input[i])):
                sum_grades += self.input[i][j][0]*self.input[i][j][1]
                sum_credits += self.input[i][j][1]

        return sum_grades/sum_credits

    def solve(self):

        #queue = [([], self.thesis[0], self.thesis[1], 30)]
        queue = [([], 0, 0, 30)]
        best_node = ([], 4, 0, 30)
        sup = 4.0

        while(len(queue) > 0):
            node = queue.pop(0)
            (del_nodes, grade, credit_sum, remaining_credits) = node
            section_index = len(del_nodes)

            if section_index == len(self.input):
                if grade <= best_node[1]:
                    best_node = node
            
            else:
                sum_grades = 0
                sum_credits = 0

                for i in range(len(self.input[section_index])):
                    sum_grades += self.input[section_index][i][0]*self.input[section_index][i][1]
                    sum_credits += self.input[section_index][i][1]

                for i in range(len(self.input[section_index])):
                    if self.input[section_index][i][1] <= remaining_credits:
                        grade_i = (grade*credit_sum+sum_grades-self.input[section_index][i][0]*self.input[section_index][i][1])/(credit_sum+sum_credits-self.input[section_index][i][1])
                        node_i = (del_nodes + [i], grade_i, credit_sum+sum_credits-self.input[section_index][i][1], remaining_credits-self.input[section_index][i][1])
                        lb = self.calc_lb(node_i)
                        ub = self.calc_ub(node_i)
                        
                        if ub < sup:
                            sup = ub

                        if(lb <= sup):
                            queue.append(node_i)
                
                node_none = (del_nodes + [-1],(grade*credit_sum+sum_grades)/(credit_sum+sum_credits), credit_sum+sum_credits, remaining_credits)
                lb = self.calc_lb(node_none)
                ub = self.calc_ub(node_none)
                
                if ub < sup:
                    sup = ub

                if(lb <= sup):
                    queue.append(node_none)

        print(self.input)
        return best_node
        