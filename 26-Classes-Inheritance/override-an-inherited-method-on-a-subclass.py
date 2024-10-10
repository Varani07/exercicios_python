class Teacher():
    def teach_class(self):
        print("Teaching stuff...")
    def grab_lunch(self):
        print("Yum yum yum!")
    def grade_tests(self):
        print("F! F! F!")

class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hooray, I'm an author!")
    def grade_tests(self):
        print("A! A! A!")

teacher = Teacher()
professor = CollegeProfessor()

teacher.teach_class()
teacher.grab_lunch()
teacher.grade_tests()
print()
professor.teach_class()
professor.grab_lunch()
professor.grade_tests()
professor.publish_book()