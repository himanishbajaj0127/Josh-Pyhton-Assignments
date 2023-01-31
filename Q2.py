'''Create arithmetics class to calculate avg, mean, mode and standard deviation'''

#Using statistics to perform the calculations as asked in the question (average, mean, mode and standard deviation)
import statistics

#Class Arithmetics has a single attribute, numbers
class Arithmetics:
    def __init__(self, numbers):
        self.numbers = numbers

    #logic to calculate average
    def avg(self):
        return sum(self.numbers) / len(self.numbers)
    #This method is an alias for the avg
    def mean(self):
        return self.avg()
    #By using the statistics.mode function from the Python Standard Library, this  method calculates mode
    def mode(self):
        return statistics.mode(self.numbers)
    #By using the statistics.stdev function from the Python Standard Library, this  method calculates Standard Deviation
    def standard_deviation(self):
        return statistics.stdev(self.numbers)

#passing list of numbers as an argument
numbers = [1, 2, 3, 4, 5]
#instance created
arithmetics = Arithmetics(numbers)

#Prints the following
print("Average: ", arithmetics.avg())
print("Mean: ", arithmetics.mean())
print("Mode: ", arithmetics.mode())
print("Standard Deviation: ", arithmetics.standard_deviation())
