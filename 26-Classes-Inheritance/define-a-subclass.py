class Store():
    def __init__(self):
        self.owner = "Matheus"

    def exclaim(self):
        return "Lots of stuff to buy!"
    
class CoffeShop(Store):
    pass

starbucks = CoffeShop()
print(starbucks.owner, " | ", starbucks.exclaim())