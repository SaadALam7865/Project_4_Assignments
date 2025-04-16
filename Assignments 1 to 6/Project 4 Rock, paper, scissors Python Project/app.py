import random
print('🎉 Welcome to the Ultimate Rock, Paper, Scissors Battle! 🎉')
print('-'*60)
print('🤖 You vs. the Mighty Computer! Let’s see who wins...')
print("\""*60)

while True:
    user_choice=input('Choose your weapon (Rock, Paper, scissors):').lower()

    if user_choice not in ['rock','paper','scissors']:
        print("It's not a valid choice..")
        continue
    computer_choice=random.choice(['rock','paper','scissors'])
    print(f'Your select {user_choice}')
    print(f'Computer select {computer_choice}')

    if user_choice == computer_choice:
        print("it's a tie!")
    elif (
     (user_choice=='rock' and computer_choice=='scissors') or
     (user_choice=='scissors' and computer_choice=='paper') or
     (user_choice=='paper' and computer_choice=='rock')

    ):
        print('You win!')
    else:
        print('Computer wins, try agian!')
    
    play_again=input("Do you want to play again (yes/no):").lower()
    if play_again != 'yes':
        print("alright!, Thanks for playing")
        print('See You!')
        break


    