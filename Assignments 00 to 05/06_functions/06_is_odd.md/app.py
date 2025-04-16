# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def print_even_odd_numbers(start, end):
    for num in range(start, end):
        if num % 2 == 0:
            print(f'{num} even!')
        else:
            print(f'{num} odd!')
        
print_even_odd_numbers(10, 20)

        

