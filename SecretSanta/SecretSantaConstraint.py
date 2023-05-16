import random

from CSP.Constraint import Constraint


class NotEqualConstraint(Constraint):
    def __init__(self, variable1, variable2):
        super().__init__([variable1, variable2])
        self.variable1 = variable1
        self.variable2 = variable2

    def is_satisfied(self):
        if self.variable1.value is None or self.variable2.value is None:
            return True
        return self.variable1.value != self.variable2.value




