
import time

# Get input from user

seconds = int(input('Enter time in seconds: '))

# Countdown loop
while seconds > 0:
    print(f'Time left: {seconds} seconds')
    time.sleep(1) # wait for 1 seconds
    seconds-=1
    
print('Times up')
