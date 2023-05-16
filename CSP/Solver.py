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
        for var in self.problem.variables:
            if not self.forward_check(var):
                print("Problem Unsolvable")
                return
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')


    def backtracking(self):
        pass
        # Write your code here

    def forward_check(self, var):
        # Write your code here
        unassignedVariables = self.problem.get_unassigned_variables();
        
        if unassignedVariables is not None:
            for variable in unassignedVariables: 
                #constraintNeighbors = self.problem.get_neighbor_constraints(variable);
                #for constraint in constraintNeighbors:
                    for value in variable._domain:
                        variable.value = value
                        if self.is_consistent(variable) is False:
                            variable._domain.remove(value)

                        variable.has_value = False;    
                        variable.value = None
    

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
        pass
        # Write your code here


    def lcv(self, var: Variable):
        pass
        # Write your code here


