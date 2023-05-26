from CSP.Constraint import Constraint

class MagicConstraintBinary(Constraint):
    def __init__(self, variables):
        super().__init__(variables)
        def is_satisfied(self):
            if variables[0].value[0] == variables[1].value[0] and variables[0].value[1] == variables[1].value[1]:
                return False
            else:
                return True
    

        