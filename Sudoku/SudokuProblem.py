from CSP.Problem import Problem
from CSP.Variable import Variable
from Sudoku.SudokuConstraint import SudokuConstraint
import os
os.system("") # needed for ANSI escape characters to work on Windows
from IPython.display import clear_output


class SudokuProblem(Problem):
    def __init__(self, grid):
        super().__init__([], [])
        variables = []
        rows = "ABCDEFGHI"
        cols = "123456789"
        domains = set(cols)

        # Create variables
        for r in rows:
            for c in cols:
                name = r + c
                value = int(grid[rows.index(r)][cols.index(c)])
                if value == 0:
                    variable = Variable(list(domains), name)
                else:
                    variable = Variable([str(value)], name, str(value))
                variables.append(variable)

        # Create constraints
        constraints = []
        # row constraints
        for r in rows:
            row_vars = [var for var in variables if var.name[0] == r]
            constraints.append(SudokuConstraint(row_vars))

        # column constraints
        for c in cols:
            col_vars = [var for var in variables if var.name[1] == c]
            constraints.append(SudokuConstraint(col_vars))

        # box constraints
        boxes = [(i, j) for i in range(0, 9, 3) for j in range(0, 9, 3)]
        for box in boxes:
            box_vars = []
            for r in range(box[0], box[0] + 3):
                for c in range(box[1], box[1] + 3):
                    box_vars.append(variables[r * 9 + c])
            constraints.append(SudokuConstraint(box_vars))

        self.constraints = constraints
        self.variables = variables



    def print_assignments(self, current_var=None):
        rows = "ABCDEFGHI"
        cols = "123456789"
        separator = "+-------+-------+-------+"

        for i in range(9):
            if i % 3 == 0:
                print(separator)
            row_str = ""
            for j in range(9):
                if j % 3 == 0:
                    row_str += "| "
                variable = self.get_variable_by_name(rows[i] + cols[j])
                value = variable.value if variable.has_value else " "
                if variable.has_initial_value:
                    row_str += "\033[1m{}\033[0m ".format(value)  # Set bold
                elif current_var is not None and current_var.name == variable.name:
                    row_str += "\033[42m{}\033[0m ".format(value)  # Set green background
                else:
                    row_str += "{} ".format(value)
            row_str += "|"
            print(row_str)
        print(separator)



