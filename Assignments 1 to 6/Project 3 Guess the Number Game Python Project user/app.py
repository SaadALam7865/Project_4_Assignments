import random
print('🎮 Welcome to the Reverse Guess the Number Game! 🤖')
print('-'*60)
print('Think of a number between 1 and 100, and I\'ll try to guess it!')
print("\""*65)

low = 1
high = 100
attempts = 0

while True:
    guess=random.randint(low, high)
    attempts+=1

    user_input= input(f'It is {guess}? (H/L/C): ').strip().upper()

    if user_input == 'H':
        high=guess-1
        print('Too High?let me try again!')
    elif user_input=='L':
        low=guess+1
        print('Too low?let me try again!')
    
    elif user_input == 'C':
        print(f'Wow, I guessed it in {attempts} tries!')
        break
    else:
        print("Please enter 'H' 'L' 'C' ")

