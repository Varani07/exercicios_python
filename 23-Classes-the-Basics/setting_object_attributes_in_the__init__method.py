class Guitar():
    def __init__(self, wood):
        self.wood = wood

acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood, electric.wood)

baritone = Guitar("Alter")

print(baritone, acoustic)