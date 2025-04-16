# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

def even_num():
    count = 0
    num = 0
    while count < 20:
        if num % 2 == 0:
            print(num)
            count += 1
            num += 1
            continue
        num += 1
        continue
    return 

even_num()

# Using for loop

print('\n')
def even_num_for():
    for num in range(0,40):
        if num % 2 == 0:
            print(num)
            continue

        
even_num_for()

# Using list comprehension

def even_num_lsit():
    
    print([i * 2 for i in range(20)])

even_num_lsit()
  
