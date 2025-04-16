import random

print('🎮 Welcome to the Reverse Guess the Number Game! 🤖')
print('-' * 60)
print('Think of a number between 1 and 100, and I\'ll try to guess it!')
print('"'.center(60, '"'))

low = 1
high = 100
attempts = 0

while low <= high:
    guess = random.randint(low, high)
    attempts += 1

    user_input = input(f'\nIs it {guess}? (H = Too High, L = Too Low, C = Correct): ').strip().upper()

    if user_input == 'H':
        high = guess - 1
        print('🔻 Too High? Let me try again...')
    elif user_input == 'L':
        low = guess + 1
        print('🔺 Too Low? Let me try again...')
    elif user_input == 'C':
        print(f'🎉 Yay! I guessed your number in {attempts} attempts!')
        break
    else:
        print("⚠️ Please enter only 'H' for high, 'L' for low, or 'C' for correct.")

else:
    print("Hmm... Something went wrong. Did you change your number mid-game? 😅")
