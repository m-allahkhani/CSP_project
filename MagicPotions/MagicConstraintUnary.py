from CSP.Constraint import Constraint

class MagicConstraintUnary(Constraint):
    def __init__(self, variable, value, index, state):
        super().__init__(variable)
        def is_satisfied(self):
            if variable.value[index] is value :
                return state
            else:
                return ~state
            