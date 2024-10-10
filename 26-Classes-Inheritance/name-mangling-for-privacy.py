class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some method")

    @property
    def attr_value(self):
        return self.__some_attribute

class SpecialNonsense(Nonsense):
    pass


n = Nonsense()
sn = SpecialNonsense()

# print(n.__some_attribute) AttributeError
# print(sn.__some_attribute) AttributeError
print(n.attr_value)
# print(n.__some_method()) AttributeError
print(n._Nonsense__some_attribute)