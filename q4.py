class MyClass:
    def __init__(self):
        pass

    def get_sublist(self,list,start,end):
        return list[start:end]

    def is_palindrome(self,string):
        return string == string[::-1]

    def has_repeated_characters(self,string):
        return len(string) != len(set(string))

# creating an object of the class
object = MyClass()

# calling the class functions
my_list = input("enter list: ")
print(object.get_sublist(my_list,1,5))
print(object.is_palindrome(input("enter string: ")))
print(object.has_repeated_characters(input("enter string: ")))