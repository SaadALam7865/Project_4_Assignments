# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
# Here's a sample run of the program (user input is in bold italics):
# Please enter an integer to be divided: 5
# Please enter an integer to divide by: 3
# The result of this division is 1 with a remainder of 2


def main():
    # Get the user input for the first number
    first_number  =  int(input('Please enter an integer to be divided: '))
    # Get the user input for the second number
    second_number =  int(input('Please enter an integer to divide by: '))

    # Calculate the result of the division
    division_result = first_number // second_number
    # Calculate the remainder of the division
    remainder_result = first_number % second_number
    # Print the result of the division and the remainder
    # Print the results
    print(f'The result of this division is {division_result} with a remainder of {remainder_result}')

    # Call the main function to run the program
if __name__ == '__main__':
    main()