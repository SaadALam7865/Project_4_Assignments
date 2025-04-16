# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

def print_divisors(num):
    for i in range(num):
        if num % (i + 1) == 0:
            print(i + 1, end=' ')
    
def main():
    num = int(input('Enter a number:' ))
    print_divisors(num)

# Call the main function
main()