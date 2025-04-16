# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

def roll_dice():
    # Simulate rolling  two dice
    die1 = random.randint(1,6) # Random number netween 1 and 6
    die2 = random.randint(1,6) # Random number between 1 and 6
    total = die1 + die2 # Calculate the total of the two dice
    return die1, die2, total # Return the values of the two dice and their total

if __name__ == '__main__':
    # Main function to run the dice rolling simulation
    print('Rolling the dice...')
    die1, die2, total = roll_dice() # Call the roll_dice function
    print(f'Die 1: {die1}')
    print(f'Die 2: {die2}')
    print(f'Total: {total}')
    