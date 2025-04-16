# Guess the number by the (Computer)
import random
print('Welcome to our guess the number game')
print('-'*50)

print("I've choose the number between 1-100 \n")
secret_num = random.randint(1,100)
attempts =0
chances = 10


while attempts < chances:
    try:
        user_guess = int( input('Enter your guess: '))
        attempts+= 1
        print('-'*50)
        if user_guess<1 or user_guess>100:
            print('Invalit input!')
        elif user_guess < secret_num:
            print('To low! try a higher number')
        elif user_guess > secret_num:
            print('To high! try a lower  number')
        else:
            print(f'Congrats  the number was: {secret_num}')
            print(f'You guessed it in {attempts} attempts.')
            break  # Exit loop if guessed correctly  
         # Inform user how many attempts are left
        print(f'Attempts left: {chances - attempts}')
    except ValueError:
        print('Please enter a valid number')
if attempts ==  chances:
         print('-' * 50)
         print(f'❌ Out of {attempts} attempts! The number was: {secret_num}')
       





