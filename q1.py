'''Q1- Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension'''

#original list
original_list = [1, 2, 3, 4, 5]

#logic for new list
new_list = [x*2 for x in original_list]

print(new_list)