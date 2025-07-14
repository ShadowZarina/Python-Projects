# Rock Paper Scissors Game

import random

selected = int(input(f"Select between rock, paper, and scissors:\n1. Rock\n2. Paper\n3. Scissors\n"))

def rps_game(selected):
    
    move = ""
    enemy_move = ""

    enemy_selected = random.randint(1,3) 
    
    match selected:
        case 1:
            move = "Rock"
        case 2:
            move = "Paper"
        case 3:
            move = "Scissors"

    match enemy_selected:
        case 1:
            enemy_move = "Rock"
        case 2:
            enemy_move = "Paper"
        case 3:
            enemy_move = "Scissors"
    
    print(f"\nYou selected {move} versus {enemy_move}!")
    
    if selected == enemy_selected:
        print("You have a draw!")

    match selected:
        case 1:
            if enemy_selected == 2:
                print("You lose!")
            elif enemy_selected == 3:
                print("You win!")
        case 2:
            if enemy_selected == 3:
                print("You lose!")
            elif enemy_selected == 1:
                print("You win!")
        case 3:
            if enemy_selected == 1:
                print("You lose!")
            elif enemy_selected == 2:
                print("You win!")

rps_game(selected)
