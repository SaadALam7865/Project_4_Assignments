import random

# Step 01
words = ['apple', 'banana', 'cherry', 'grape', 'orange']
word = random.choice(words)
guessed_letter = []  # Changed variable name for better readability
tries = 6

print('Welcome to Hangman!')
print('_ ' * len(word))

# Step 2
while tries > 0:
    guess = input('Enter a letter: ').lower()

    if guess in guessed_letter:
        print('You already guessed that letter..')
        continue

    guessed_letter.append(guess)

    if guess in word:
        print("Correct! Mobarak")
    else:
        print('Wrong!')
        tries -= 1
        print(f'Tries left: {tries}')
    
    # Show current progress!
    display_word = ""
    for letter in word:
        if letter in guessed_letter:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word.strip())

    # Check if the word is fully guessed
    if all(letter in guessed_letter for letter in word):
        print('Congratulations! You Won🎉')
        break

else:
    print(f'You lost the game! The word was: {word}')
