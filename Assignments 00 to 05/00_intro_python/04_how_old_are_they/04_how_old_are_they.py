
# Problem Statement
# Write a program to solve this age-related riddle!
# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
# Anton is 3
# Beth is 4
# Chen is 5
# Drew is 6
# Ethan is 7

# Plan 
def main():
    # Define the ages of the friends
    anton_age = 21
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = anton_age + chen_age
    ethan_age = chen_age
    # Print the names and ages of the friends
    print(f'Anton is {anton_age}')
    print(f'Beth is {beth_age}')
    print(f'Chen is {chen_age}')
    print(f'Drew is {drew_age}')
    print(f'Ethan is {ethan_age}')
    
    # Call the main function to execute the program
if __name__ == '__main__':
    main()




