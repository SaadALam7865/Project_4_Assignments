# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# We start by creating an empty dictionary.

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == '':
            break
        number = input('Number: ')
        phonebook[name] = number  # Store name-number pair
    
    return phonebook  # Move return statement outside loop

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f'{name}: {number}')

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input('Enter name to lookup: ')
        if name == '':
            break
        if name not in phonebook:
            print(name + " is not in the phonebook.")
        else:
            print(f'{name}\'s Number: {phonebook[name]}')

def main():
    phonebook = read_phone_numbers()  # Read phone numbers
    print_phonebook(phonebook)  # Print all phonebook entries
    lookup_numbers(phonebook)  # Lookup numbers
    print('Goodbye!')

if __name__ == "__main__":
    main()
