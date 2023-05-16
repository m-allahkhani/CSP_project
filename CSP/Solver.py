import os
import subprocess
import time
from collections import deque
from copy import deepcopy
from typing import Optional

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem, use_mrv=False, use_lcv=False, use_forward_check=False):
        self.problem = problem
        self.use_lcv = use_lcv
        self.use_mrv = use_mrv
        self.use_forward_check = use_forward_check

    def is_finished(self) -> bool:
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        self.problem.calculate_neighbors()
        start = time.time()
        # for var in self.problem.variables:
        #     if not self.forward_check(var):
        #         print("Problem Unsolvable")
        #         return
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')


    def backtracking(self):
        var = self.select_unassigned_variable()
        if var is None:
            return True
        for value in var.domain:
            var.value = value
            if self.is_consistent(var) is True:
                result = self.backtracking()
                if result is True:
                    return True
            var._has_value = False
            var.value = None
        return False

    def forward_check(self, var):
        pass
        # Write your code here

    def select_unassigned_variable(self) -> Optional[Variable]:
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None

    def order_domain_values(self, var: Variable):
        if self.use_lcv:
            return self.lcv(var)
        return var.domain

    def mrv(self) -> Optional[Variable]:
        pass
        # Write your code here

    def is_consistent(self, var: Variable):
        for con in self.problem.get_neighbor_constraints(var):
            if con.is_satisfied() is False:
                return False
        return True


    def lcv(self, var: Variable):
        pass
        # Write your code here


