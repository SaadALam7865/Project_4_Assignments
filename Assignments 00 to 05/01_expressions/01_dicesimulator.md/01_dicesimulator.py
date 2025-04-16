# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
# It also shows how to use the random module to generate random numbers.
import random

def roll_dice():
    # Simulate rolling two dice, three times
    for _ in range(3):
        print('Rolling the dice...')
        die1 = random.randint(1,6) # Roll the firt die
        die2 = random.randint(1,6) # Roll the second die
        print(f'Die 1: {die1}, Die 2: {die2}') # Print the results of the roll
        # This inner function has access to the variables defined in its enclosing scope (the outer function)
        total = die1 + die2 # Calculate the ttotl of the two dice
        print(f'Total: {total}')

if __name__ == '__main__':
    roll_dice() 
