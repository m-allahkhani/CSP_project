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
        if self.use_mrv:
            self.problem.calculate_degree()
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
        domain_order = self.order_domain_values(var)
        
        for value in domain_order:
            var.value = value
            removeValues = {}
            unassignedVariables = self.problem.get_unassigned_variables()
            if self.is_consistent(var) is True:
                if self.use_forward_check is True: 
                   self.forward_check(var, removeValues, unassignedVariables);
                result = self.backtracking()
                if result is True:
                    return True
            if self.use_forward_check is True:
                self.add_remove_values(unassignedVariables,removeValues)
                
            var._has_value = False
            var.value = None
            
        return False

    def forward_check(self, var, removeValues, unassignedVariables):
        
        if unassignedVariables is not None:
            for variable in unassignedVariables : 
                    name_var = variable.name
                    removeValues[name_var] = []
                    for value in variable._domain:
                        variable.value = value
                        if self.is_consistent(variable) is False:
                            variable._domain.remove(value)
                            removeValues[name_var].append(value)

                        variable._has_value = False;    
                        variable.value = None

                  
    
    def add_remove_values(self, variables: list, removeValues):

        for var in variables:
            name_var = var.name
            if name_var in removeValues:
                var.domain.extend(removeValues[name_var])


    def select_unassigned_variable(self) -> Optional[Variable]:
        if self.use_mrv:
            return self.mrv()
        unassigned_variables = self.problem.get_unassigned_variables()
        return unassigned_variables[0] if unassigned_variables else None


    def mrv(self) -> Optional[Variable]:
        variables = self.problem.get_unassigned_variables()
        for var in variables:
            var.mrv_val = len(var.domain)
            #variable.degree_val = len(self.get_neighbor_constraints(variable))
        variables = sorted(variables, key=lambda obj: (obj.mrv_val, -obj.degree_val))
        return variables[0] if variables else None


    def is_consistent(self, var: Variable):
        for con in self.problem.get_neighbor_constraints(var):
            if con.is_satisfied() is False:
                return False
        return True

    def lcv(self, var: Variable):
        domain_list = []

        for value in var._domain:
            conflict = self.count_conflicts(var, value)
            domain_list.append((value, conflict))
            
        sorted_domain = sorted(domain_list, key = lambda x: x[1], reverse = False)
        return [index[0] for index in sorted_domain]


    def count_conflicts(self, var:Variable, value):
        count = 0 
        var.value = value
        neighbors = self.problem.get_unassigned_variables()

        for neighbor in neighbors:
            for value in neighbor._domain:
                neighbor.value = value
                if self.is_consistent(neighbor) is False:
                    count+=1
                    break
            neighbor._has_value = False
            neighbor.value = None
                
        var._has_value = False; 
        var.value = None
        return count
    
    def order_domain_values(self, var: Variable):
        if self.use_lcv:
            return self.lcv(var)
        else:
            return var._domain
        
        


