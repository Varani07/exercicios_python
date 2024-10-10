class Employee():
    def do_work(self):
        print("I am working!")

class Manager(Employee):
    def waste_time(self):
        print("Wow! This youtube video looks fun!")

class Director(Manager):
    def fire_employee(self):
        print("You're Fired!")

e = Employee()
m = Manager()
d = Director()

e.do_work()
print("")
m.do_work()
m.waste_time()
print("")
d.do_work()
d.waste_time()
d.fire_employee()