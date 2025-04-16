# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# The function should not return anything, it should just print the first element in the list.
# all elments agr print krna ho tu
def get_first_element(lst):
    # Your code here
    print(lst)
    pass
# Propmt the user to input the list..
lst = []
while True:
    try:
        element = input('Enter an element (or press Enter to finish): ')
        if element == '':
            break
        # Check if the element is a number
        elif element ==  int(element):
            lst.append(int(element))
            break
        lst.append(element)
    except EOFError:
        break
    # Call the function
    print(f'The first element in the list is: {lst[0]} ')
    get_first_element(lst)


