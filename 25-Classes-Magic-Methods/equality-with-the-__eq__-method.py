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
        
bob = Student(math=90, history=90, writing=90)
moe = Student(math=100, history=80, writing=90)
joe = Student(math=40, history=54, writing=60)

print(bob.grades, moe.grades, joe.grades)
print(bob == moe, moe == bob, joe == moe)
print(bob != moe, moe != bob, joe != moe)