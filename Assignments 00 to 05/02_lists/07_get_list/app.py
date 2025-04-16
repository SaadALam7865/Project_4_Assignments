# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    values = [] # Initialize an empty list to store values
    while True:
        value = input('Enter a value: ') # Prompt the user for input
        if value == '':
            break
        values.append(value)
        print('Here is the list:', values) # Print the current list after each
        print(f'Current list: {values}') 
        print(f'Length of list: {len(values)}') # Print the length of the list  after each entry
        print('' + '-' * 20)

if __name__ == '__main__':
    main()