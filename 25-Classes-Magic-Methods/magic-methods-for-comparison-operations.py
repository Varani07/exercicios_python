class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student):
        return self.grades == other_student.grades
    
    def __gt__(self, other_student):
        return self.grades > other_student.grades
    
    def __lt__(self, other_student):
        return self.grades < other_student.grades
    
    def __add__(self, other_student):
        return self.grades + other_student.grades
    
    def __sub__(self, other_student):
        return self.grades - other_student.grades
    
    def __mul__(self, other_student):
        return self.grades * other_student.grades
    
    def __truediv__(self, other_student):
        return self.grades / other_student.grades
        
bob = Student(math=90, history=90, writing=90)
moe = Student(math=100, history=80, writing=90)
joe = Student(math=40, history=54, writing=60)

print(bob.grades, moe.grades, joe.grades)
print(bob == moe, moe == bob, joe == moe)
print(bob != moe, moe != bob, joe != moe)
print(bob == moe == joe)
print(bob - joe)
print(moe > joe, joe < moe, moe < joe)
print(bob + moe, bob/joe, bob*joe)
# help(8)

# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, 
# a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object.
# The choice of whether to use protected attributes is up to you.

# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
#    "You paid 24.99 to Greyhound to go to Boston.""
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price.
# These are all fed in as arguments when a BusTrip object is initialized.

# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.
class BusTrip():
    def __init__(self, destination, company, price):
        self._destination = destination
        self._company = company
        self._price = price
    def __str__(self):
        return f"You paid {self._price} to {self._company} to go to {self._destination}."
    def __eq__(self, other_value):
        if self._price >= other_value._price:
            difference = self._price - other_value._price
        else:
            difference = other_value._price - self._price
        return self._destination == other_value._destination and difference <= 3
    # Código do Professor
    # def __eq__(self, other_value):
    #     difference = abs(self._price - other_value._price)
    #     return self._destination == other_value._destination and difference <= 3