# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# The conversion formula is:
# inches = feet * 12

def feet_to_inches(feet):
    """
    Convert feet to inches.
    
    :param feet: The number of feet to convert.
    :return: The equivalent numbe of inches."""
    return feet * 12

# Example usage:
if __name__ == '__main__':
    feet = float(input('Enter the number of feet: '))
    inches = feet_to_inches(feet)
    print(f'{feet} feet is equal to {inches} inches.')
    