
import time
from colorama import init, Fore, Style

init(autoreset=True)  # Automatically reset colors after each print

# --- Inputs ---
print(Fore.CYAN + "Let's build your story...\n")
time.sleep(1)

name = input(Fore.YELLOW + "Enter your name: ")
something = input(Fore.YELLOW + "Name something you once disliked: ")
negative_feel = input(Fore.YELLOW + "How did it feel? ")
object = input(Fore.YELLOW + "Mention an object that intrigued you: ")
content = input(Fore.YELLOW + "What was inside it? ")
lesson_learned = input(Fore.YELLOW + "A life lesson in a few words: ")
challenge = input(Fore.YELLOW + "Another word for a challenge: ")
positive_outcome = input(Fore.YELLOW + "A word for a positive change: ")

# --- Dramatic Reveal ---
print("\n" + Fore.GREEN + "Generating your story...")
time.sleep(2)
print(Fore.MAGENTA + "\n--- Your Mad Lib Story ---\n")
time.sleep(1)

# --- Story Output ---
print(Fore.CYAN + f"{name} once hated {something}, and it made them feel {negative_feel}.")
time.sleep(2)
print(Fore.CYAN + f"But one day, they stumbled upon a mysterious {object}...")
time.sleep(2)
print(Fore.CYAN + f"Inside it was something unexpected: {content}.")
time.sleep(2)
print(Fore.CYAN + f"That moment changed everything. It taught {name} this simple truth: ")
time.sleep(2)
print(Fore.YELLOW + Style.BRIGHT + f"'{lesson_learned}'")
time.sleep(2)
print(Fore.CYAN + f"Since then, every {challenge} became a step toward {positive_outcome}.")
time.sleep(2)
print(Fore.GREEN + Style.BRIGHT + "And life? It started to feel like a beautiful surprise every single day.")
print(Fore.BLUE + Style.DIM + "\n--- The End ---")
