# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length. 


def get_last_element(lst):
    # Useing the index -1 to get the last element of the list
    last_element = lst[-1]
    print(last_element)
    # REturning the last element of the list
    return last_element

# Test the function with a list
test_list = [1, 2, 3, 4, 5]
get_last_element(test_list) 

