# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

# Test the function with a list of numbers
numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers)
print(f'The sum of {numbers} is {result}.')