print(type({"a":1}))
print(isinstance(1, int), isinstance(" ", int), isinstance({"a": 1}, dict))

print(isinstance(1, object), isinstance(str, object), isinstance(max, object))
print(isinstance([], (list, dict)), isinstance([], (int, str)))

class Person():
    pass

class Superhero(Person):
    pass

arnold = Person()
boris = Superhero()

print(isinstance(boris, Superhero), isinstance(boris, Person))
print(isinstance(arnold, Person), isinstance(arnold, Superhero))

print()
print(issubclass(Superhero, Person), issubclass(Person, Superhero))
print(issubclass(Person, object), issubclass(Superhero, object))