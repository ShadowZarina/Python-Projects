# Number Guesser

import random

a = int(input("Enter the minimum value: "))
b = int(input("Enter the maximum value: "))
guess = int(input(f"Guess a number from {a} to {b}: "))

def guessing_game(a,b,guess):
    
    tries = 0
    secret_number = random.randint(a, b) 
    
    while tries < 3:
        if guess == secret_number:
            print("\nCongrats! You guessed right!\n")
            break
        else:
            print("\nTry again!")
            tries += 1
            if tries < 3:
                guess = int(input(f"Guess again (({3-tries} tries left): "))
            else:
                print(f"\nSorry, you've run out of tries. The correct number was {secret_number}!\n")

guessing_game(a,b,guess)
