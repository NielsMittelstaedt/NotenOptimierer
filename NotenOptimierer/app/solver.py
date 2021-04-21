from ortools.linear_solver import pywraplp

class Solver:
    def __init__(self, test):
        self.test = test
        self.solver = pywraplp.Solver.CreateSolver('SCIP')

    def setupSolver(self):
        infinity = self.solver.infinity()
        self.x = self.solver.IntVar(0.0, infinity, 'x')
        self.y = self.solver.IntVar(0.0, infinity, 'y')
        
        # Create a linear constraint, 0 <= x + y <= 2.
        ct = self.solver.Constraint(0, 2, 'ct')
        ct.SetCoefficient(self.x, 1)
        ct.SetCoefficient(self.y, 1)

        # Create the objective function, 3 * x + y.
        self.objective = self.solver.Objective()
        self.objective.SetCoefficient(self.x, 3)
        self.objective.SetCoefficient(self.y, 1)
        self.objective.SetMaximization()

    def solve(self):
        self.solver.Solve()
        print('Solution:')
        print('Objective value =', self.objective.Value())
        print('x =', self.x.solution_value())
        print('y =', self.y.solution_value())