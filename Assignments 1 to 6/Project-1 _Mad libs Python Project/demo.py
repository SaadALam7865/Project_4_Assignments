# Python projects --MAd libs 

print('Welcome to our story creator')
print('-'* 60)

name = input("Enter your name: ")
something=input('Name something you once disliked. ')
negative_feel = input("How did it feel? ")
object = input("Mention an object that intrigued you.")
content = input("What was inside it? ")
lesson_learned = input("A life lesson in a few words? ")
challenge = input("Another word for a challenge? ")
positive_outcome = input('A word for a positive change? ')

print("\n--- Your Mad Lib Story ---\n")

print(f'{name} once hated failure, and it made them feel {negative_feel}.')
print(f'But one day, they stumbled upon a mysterious {object}.')
print(f'Inside it was something unexpected: {content}.')
print(f'That moment changed everything. It taught {name} this simple truth: {lesson_learned}')
print(f'Since then, every {challenge} became a step toward {positive_outcome}.')
print(f'And life? It started to feel like a beautiful surprise every single day.')
