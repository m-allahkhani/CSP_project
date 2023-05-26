
from CSP.Problem import Problem
from CSP.Variable import Variable
from MagicPotions.MagicConstraintBinary import MagicConstraintBinary
from MagicPotions.MagicConstraintUnary import MagicConstraintUnary



class MagicProblem(Problem):
    def __init__(self):
        super().__init__([], [], "MagicProblem")
        domain = [("green","acid"), ("green","poison"), ("green","healer"), ("green","transformation"), ("green","invisible"),
                  ("red","acid"),   ("red","poison"),   ("red","healer"),   ("red","transformation"),   ("red","invisible"),
                  ("black","acid"), ("black","poison"), ("black","healer"), ("black","transformation"), ("black","invisible"),
                  ("blue","acid"),  ("blue","poison"),  ("blue","healer"),  ("blue","transformation"),  ("blue","invisible"),
                  ("purple","acid"),("purple","poison"),("purple","healer"),("purple","transformation"),("purple","invisible")]

        aldo = Variable[str](domain, "Aldo")
        beatrice = Variable[str](domain, "Beatrice")
        ignatius = Variable[str](domain, "Ignatius")
        lorenzo = Variable[str](domain, "Lorenzo")
        ursula = Variable[str](domain, "Ursula")

        unaryC1  = MagicConstraintUnary(aldo, 'red', 0, False)
        unaryC2  = MagicConstraintUnary(aldo, 'green', 0, False)
        unaryC3  = MagicConstraintUnary(aldo, 'transformation', 1, True)

        unaryC4  = MagicConstraintUnary(beatrice, 'blue', 0, True)
        unaryC5  = MagicConstraintUnary(beatrice, 'acid', 1, False)
        unaryC6  = MagicConstraintUnary(beatrice, 'healer', 1, False)

        unaryC7  = MagicConstraintUnary(ignatius, 'purple', 0, False)
        unaryC8  = MagicConstraintUnary(ignatius, 'black', 0, False)
        unaryC9  = MagicConstraintUnary(ignatius, 'poison', 1, True)

        unaryC10 = MagicConstraintUnary(lorenzo, 'green', 0, True)
        unaryC11 = MagicConstraintUnary(lorenzo, 'poison', 1, False)

        unaryC12 = MagicConstraintUnary(ursula, 'blue', 0, False)
        unaryC13 = MagicConstraintUnary(ursula, 'black', 0, False)
        unaryC14 = MagicConstraintUnary(ursula, 'invisible', 1, True)

        binaryC1  = MagicConstraintBinary([aldo, beatrice])
        binaryC2  = MagicConstraintBinary([aldo, ignatius])
        binaryC3  = MagicConstraintBinary([aldo, lorenzo])
        binaryC4  = MagicConstraintBinary([aldo, ursula])
        binaryC5  = MagicConstraintBinary([beatrice, ignatius])
        binaryC6  = MagicConstraintBinary([beatrice, lorenzo])
        binaryC7  = MagicConstraintBinary([beatrice, ursula])
        binaryC8  = MagicConstraintBinary([ignatius, lorenzo])
        binaryC9  = MagicConstraintBinary([ignatius, ursula])
        binaryC10 = MagicConstraintBinary([lorenzo, ursula])

        self.variables = [aldo, beatrice, lorenzo, ignatius, ursula]
        self.constraints = [unaryC1, unaryC2, unaryC3, unaryC4, unaryC5, unaryC6, unaryC7, 
                            unaryC8, unaryC9, unaryC10, unaryC11, unaryC12, unaryC13, unaryC14,
                            binaryC1, binaryC2, binaryC3, binaryC4, binaryC5, binaryC6, binaryC7,
                            binaryC8, binaryC9, binaryC10]
                            

        def print_assignments(self):
            for variable in self.variables:
                print(f"{variable.name}'s potion is {variable.value[0]} and {variable.value[1]}")






