import random
from typing import List

from CSP.Problem import Problem
from CSP.Variable import Variable
from SecretSanta.SecretSantaConstraint import NotEqualConstraint


class SecretSantaProblem(Problem):
    def __init__(self, participants: List[str]):
        super().__init__([], [], f"Secret Santa With {len(participants)} Participants")

        self.participants = participants
        for participant in participants:
            domain = [p for p in self.participants if p != participant]
            variable = Variable(domain, participant)
            self.variables.append(variable)

        self.constraints = [NotEqualConstraint(p1, p2) for p1 in self.variables for p2 in self.variables if p1.name != p2.name]

    def assign_givers_and_receivers(self):
        # Shuffle participants to avoid deterministic solutions
        random.shuffle(self.participants)

        # Assign givers and receivers
        for i in range(len(self.variables)):
            self.variables[i].value = self.variables[(i+1) % len(self.variables)].name

    def print_assignments(self):
        for participant in self.variables:
            print(f"{participant.name} will give a gift to {participant.value}")


