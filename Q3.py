class AgeException(Exception):
    pass
def validate_age(age):
    if age<18:
        raise AgeException("Age is less than 18, sorry you can not vote")

    else:
        print("Valid Age to vote")

try:
    age = int(input("enter age: "))
    validate_age(age)
except AgeException as ae:
    print(ae)