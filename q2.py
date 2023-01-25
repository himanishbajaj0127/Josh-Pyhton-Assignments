# Global solution
# taking input from user as a string
string = str(input("enter string: "))

# casefold is a in-built converts the uppercase letters into lower case
string = string.casefold()

# reversed in a in-built function to reverse a string
rev_str = reversed(string)

#condition applied to get whether the entered string is a palindrome or not
if list(string) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")