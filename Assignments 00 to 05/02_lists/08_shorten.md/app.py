# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.




# There is no need to edit code beyond this point



MAX_LENGTH = 3  # Set the maximum length

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH"""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove last item
        print(f"Removing {removed_item}")  # Print removed item

# Testing function
def main():
    test_list = [10, 20, 30, 40, 50, 60, 70]  # Example list
    shorten(test_list)
    print("Final list:", test_list)

main()
