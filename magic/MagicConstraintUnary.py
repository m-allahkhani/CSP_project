from CSP.Constraint import Constraint

class MagicConstraintUnary(Constraint):
    def __init__(self, variable, value, index, state):
        super().__init__([variable])
        self.value = value
        self.index = index
        self.state = state
        
    def is_satisfied(self):
        if self.variables[0].value[self.index] is self.value :
            return self.state
        else:
            return not self.state
            