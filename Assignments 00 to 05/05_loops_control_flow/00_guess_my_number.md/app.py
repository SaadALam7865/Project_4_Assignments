
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48




def guess_number():
    low = 0
    high = 99
    chances = 10  # Maximum attempts
    secret_number = (low + high) // 2  # The number to be guessed

    print(f"I am thinking of a number between {low} and {high}... Try to guess it!")

    for attempt in range(1, chances + 1):
        user_guess = int(input(f"Attempt {attempt}/{chances} - Enter your guess: "))

        if user_guess < secret_number:
            print("Your guess is too low.")
            low = user_guess + 1  # Update the lower bound

        elif user_guess > secret_number:
            print("Your guess is too high.")
            high = user_guess - 1  # Update the upper bound

        else:
            print(f"🎉 Congrats! You guessed the number {secret_number} correctly in {attempt} attempts.")
            return  # Exit function on correct guess

    print(f"❌ You've run out of attempts! The correct number was {secret_number}.")

if __name__ == '__main__':
    guess_number()
