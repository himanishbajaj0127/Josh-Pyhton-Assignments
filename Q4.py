class LoanEligibilityException(Exception):
    pass

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def CheckLoanEligibility(self):
        if self.salary<10000:
            raise LoanEligibilityException("You are not eligible due to salary less tha 10k")
        else:
            print("you are eligible for loan!")

try:
    name = input("enter name: ")
    salary = int(input("enter you salary per month: "))
    Person = Person(name,salary)
    Person.CheckLoanEligibility()

except LoanEligibilityException as lee:
    print(lee)