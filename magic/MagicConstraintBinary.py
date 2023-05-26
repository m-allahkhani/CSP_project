from CSP.Constraint import Constraint

class MagicConstraintBinary(Constraint):
    def __init__(self, variables):
        super().__init__(variables)
    def is_satisfied(self):
        
        if self.variables[0].value is None or self.variables[1].value is None:
            return True
        if (self.variables[0].value[0] ==  self.variables[1].value[0]) or (self.variables[0].value[1] == self.variables[1].value[1]):
            return False
        else:
            return True
    

        