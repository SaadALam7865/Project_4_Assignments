# Write a function that takes two numbers and finds the average between the two.

def average(num1, num2):
    """Calculate the average of two numbers."""
    return (num1 + num2) / 2

# Test the function
if __name__ == '__main__':
    num1 = int(input('Enter the first number: '))   
    num2 = int(input('Enter the second number: ')) 
    result = average(num1, num2)
    print(f'The average of {num1} and {num2} is {result}!')
