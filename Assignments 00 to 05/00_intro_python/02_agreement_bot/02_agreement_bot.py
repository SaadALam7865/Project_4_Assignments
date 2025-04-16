# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!

def favorite_animal():
    # Ask the user for their favorite animal
    animal = input('What\'s your favorite animal? ')
    if animal == "":
        print(" Please enter a valid animal name.")
    elif animal.isdigit():
       print('Please enter a valid animal name...')
    else:
        # REspond with the user's favorite animal
       print(f'My favorite animal is also {animal}!')


# Call the function to run the program
if __name__ == '__main__':
    favorite_animal()
    