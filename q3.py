'''Q3- Build a counter generator'''

#takes two optional arguments, start and step, 
# which specify the starting value and the step size
def count_generator(start=0, step=1):
    current = start
    while True:
        yield current
        current += step
#generator instance counter
counter = count_generator(start=0, step=1)

#loop to print the first 5 values.
for i in range(5):
    print(next(counter))