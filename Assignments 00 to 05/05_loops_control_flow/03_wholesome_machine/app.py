# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!
# Here's a sample run of the program (user input is in blue):
# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)
# Note that you can call input() with no prompt and it will still wait for a user to type something!

AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    
    user_feedback = input()  # Get initial user input

    while user_feedback != AFFIRMATION:  # Compare with the correct affirmation
        print("Hmmm, that was not the affirmation. Please try again:")
        user_feedback = input()  # Ask for input again

    print("That's right! ✅ Keep believing in yourself. 💪")

if __name__ == "__main__":
    main()





