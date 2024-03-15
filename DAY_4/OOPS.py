# Day 4(07-03-2024)
# oops4

class Employee:
    # constructors
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def getSalary(self):
        return self.salary

rohan = Employee("Rohan", 34566)
print(rohan.getSalary())
print(rohan.name)

        