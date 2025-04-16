# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
# An example run of the program looks like this (user input is in blue):
# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def get_user_numbers():
      """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
      user_numbers = []
      while True:
            user_input = input('Enter a number: ')

            if user_input == '':
                  break
                # convert the user input to an integer and add it to the list
            
            num = int(user_input)
            user_numbers.append(num)

      return user_numbers

def count_numbers(num_list):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict = {
          
    }
    for num in num_list:
          if num in num_dict:
                num_dict[num] += 1
          else:
              num_dict[num] = num_dict.get(num, 0) + 1  # This is a more efficient way to increment a value in a dictionary.  It uses the get method to retrieve the value, if it exists, and then adds 1. If it doesn't exist, it returns 0 and adds 1.

    return num_dict

def print_number_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value."
    """
    for num, count in num_dict.items():
          print(f'{num} appears {count} times.')

def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = get_user_numbers()
    num_dict = count_numbers(user_numbers)
    print_number_counts(num_dict)

# Python boilerplate.
if __name__ == '__main__':
     main()
