# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
# The first even number is 0:
# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


# Approach 1: Using a for loop
def print_even_numbers_for():
    for i in range(20):
        print(i * 2, end='')
        if i < 19:  # Check if its not the last number to avoid trailing space
            # Print a space after every other number except the last one
            print('', end='')
            # Print a space after every other number except the last one
            print(' ', end='')
        else:
            print('')

# Approach 2: Using a while loop

def print_even_numbers_while():
    i = 0
    while i < 20:
        print(i * 2 , end=' ')
        i += 1
        print('')
        if i < 20:
            print(' ', end='')
        else:
            print('')


# Approach 3: Using a list comprehension
def print_even_numbers_list_comprehension():
    even_numbers = [i * 2 for i in range(20)]
    print(' '.join(map(str, even_numbers)))
    print('')

# Approach 4: Using a generator expression
def print_even_numbers_generator():
    even_numbers = (i * 2 for i in range(20))
    print(' '.join(map(str, even_numbers)))
    print('')

# Run each approach
print("Using for loop:")
print_even_numbers_for()
print('\n')
print("Using while loop:")
print_even_numbers_while()
print('\n')
print("Using list comprehension:")
print_even_numbers_list_comprehension()
print('\n')
print("Using generator expression:")
print_even_numbers_generator()

