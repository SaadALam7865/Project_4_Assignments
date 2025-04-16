# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def count_even(lst):
    """Returns number of even numbers in list."""
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count  # Final count return karna chahiye

def get_list_of_ints():
    '''Reads in integers until the user presses enter and returns the resulting list.'''
    lst = []
    while True:
        user_input = input('Enter an integer or press enter to stop: ')
        if user_input == '':
            break  # Jab user blank input de to loop se bahar
        elif user_input == str:
            print('Please enter a valid integer.')
        try:
            lst.append(int(user_input))
        except ValueError:
            print('Please enter a valid integer.')
    return lst

def main():
    '''Main function to run the program.'''
    lst = get_list_of_ints()  
    even_count = count_even(lst)
    print('The number of even numbers in the list is:', even_count)

main()

    


   
