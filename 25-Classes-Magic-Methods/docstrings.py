import sushi
import math

# print(sushi.__doc__)
# print(sushi.fish.__doc__)
# print(sushi.Salmon.__doc__)
# print(sushi.Salmon.bake.__doc__)

# print(math.__doc__)
# print(math.sqrt.__doc__)

help(sushi)
# help(sushi.fish)

# Define a CollegeStudent class that accepts and assigns a university attribute.

# Add a docstring for the class equal to "Blueprint for a student at an institution of higher learning"

# Define three instance methods — sleep, eat, and party. 
# The actual content of the methods is irrelevant (feel free to use the pass keyword)

# The sleep method should have the docstring "Sleep through class".
# The eat method should have the docstring "Go to the cafeteria".
# The party method should have the docstring "Hit the books hard".

# To simplify the test evaluation, submit ALL docstrings without any line breaks.
# Example: """Sample docstring"""
# You're welcome to use single quotes, double quotes, or triple quotes.
class CollegeStudent():
    """Blueprint for a student at an institution of higher learning"""
    def __init__(self, university):
        self._university = university
    def sleep(self):
        """Sleep through class"""
        pass
    def eat(self):
        """Go to the cafeteria"""
        pass
    def party(self):
        """Hit the books hard"""
        pass