# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

def double_numbers(numbers):
    return [num * 2 for num in numbers] # List comprehension to double each number in the list
numbers = [1, 2, 3, 4]
res = double_numbers(numbers)
print(f'The list of numbers is: {numbers} and the doubled list is: {res}')
