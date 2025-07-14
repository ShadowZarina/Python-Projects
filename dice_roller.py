# Digital Dice Roller

import random

number = int(input("How many dice do you want rolled? "))

def dice_roll(number):
 
    sum = 0

    for i in range(number):
        roll = random.randint(1,6)
        print(f"Roll {i + 1}: {roll}")
        sum += roll

    print(f"Total value of rolls: {sum}")

dice_roll(number)
