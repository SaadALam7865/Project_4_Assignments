# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
# Here's a sample run of the program (user input is in bold italics):
# What is the length of side 1? 3
# What is the length of side 2? 4
# What is the length of side 3? 5.5
# The perimeter of the triangle is 12.5

# The perimeter of a triangle is the sum of the lengths of its three sides.

def main():
    # Get the lengths of the sides from the user
    side1 = float(input('What is the length of side 1?'))
    side2 = float(input("what is the length of side 2?"))
    side3 = float(input('Whst is the length of side 3?'))
    # Calculate the perimeter
    perimeter = side1 + side2 + side3
    # Print the perimeter
    print('The perimeter of the triangle is', perimeter)

# Call the main function to run the program
if __name__ == '__main__':
    main()