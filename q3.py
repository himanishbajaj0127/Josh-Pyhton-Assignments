#Global solution

#Taking string input from user
string = str(input("enter string: "))

#Using list() and set() methods
x=list(set(string))
y=list(string)

#sort() method sorts the list ascending by default
x.sort()
y.sort()

#applying a conditont to check whether the entered string contains repeated letters or not
if(x==y):
	print("does not contain repeated letters ")
else:
	print("contains repeated letters")
