#Judah Brogdon
#Ms. Amaya
#Python section A
#8 May 2025


import random
import time
import os
from playsound3 import playsound

#input:None
#return:None
#purpose: To welcome the user
def welcome():
    print("Welcome to rock, paper, scissors! ")
    print("To exit type 'exit'\n")

#input: None
#return: String
#purpose: to choose computer move
def pick_move():
    print("Picking Move...")
    time.sleep(2)
    print("Move Picked!\n")
    moves = ["rock", "paper", "scissors"]
    choice = random.choice(moves)
    return (choice)
    
#input: string
#return: string
#purpose: to get the users move
def user_move():
    while True:
        user_choices = input("What move will you do? rock/paper/scissors: ")
        if user_choices.isalpha:
            user_choice = user_choices.casefold()
            if user_choice == "exit":
                return (user_choice)
            elif user_choice == "rock":
                return (user_choice)
            elif user_choice == "paper":
                return user_choice
            elif user_choice == "scissors":
                return (user_choice)
            else:
                print(f"{user_choice} is not a valid input, please enter a valid input. ")
        else:
            print(f"{user_choices} is not a valid input, please enter a valid input. ")

#input: None
#return: string
#purpose: to determine winner
def Winner(choice, user_choice):
    
    if choice == "rock" and user_choice == "scissors":
        winner = "Computer!"
        return winner

    elif choice == "scissors" and user_choice == "paper":
        winner = "Computer!"
        return winner
    
    elif choice == "paper" and user_choice == "rock":
        winner = "Computer!"
        return winner
    
    elif choice == "scissors" and user_choice == "rock":
        winner = "Player!"
        return winner
    
    elif choice == "paper" and user_choice == "scissors":
        winner = "Player!"
        return winner
    
    elif choice == "rock" and user_choice == "paper":
        winner = "Player!"
        return winner
    
    elif choice == "rock" and user_choice == "rock":
        winner = "It's A Tie!"
        return winner
    
    elif choice == "scissors" and user_choice == "scissors":
        winner = "It's A Tie!"
        return winner
    
    elif choice == "paper" and user_choice == "paper":
        winner = "It's A Tie!"
        return winner
    
#input: None 
#return: None
#purpose: to make game visually appealing and show winner
def game(choice, user_choice, winner):
    print("\n")
    time.sleep(1)
    print("Rock!")
    time.sleep(1)
    print("Paper!")
    time.sleep(1)
    print("Scissors!")
    time.sleep(1)
    print("SHOOT!\n")
    time.sleep(1)

    print(f"Your choice: {user_choice}")
    time.sleep(1)
    print(f"The computers choice: {choice}\n")
    time.sleep(1)

    print("Computing Winner...")
    time.sleep(2)
    print("And the winner is!!")
    playsound("065391_drumrollwav-88344.mp3", block=False)
    time.sleep(5)
    print(winner)
    print("\n")
    time.sleep(1)

#input: None
#return: None
#purpose: To run the game
def main():
    wins = 0
    computer = 0
    ties = 0
    while True:
        sound = playsound("big-band-show-146321 (1).mp3", block=False)
        welcome()
        time.sleep(1)
        choice = pick_move()
        time.sleep(1)
        user_choice = user_move()
        if user_choice == "exit":
                print("Thank you for playing!")
                print("Exiting Program...")
                time.sleep(2)
                return
        winner = Winner(choice, user_choice)
        if winner == "Player!":
            wins = wins + 1
        elif winner == "Computer!":
            computer = computer + 1
        else:
            ties = ties + 1
        game(choice, user_choice, winner)
        time.sleep(1)
        print(f"You have won {wins} times! ")
        time.sleep(1)
        print(f"The computer has won {computer} times! ")
        time.sleep(1)
        print(f"The game has tied {ties} times! ")
        print("\n\n")
        time.sleep(4)
        print("Resetting Game...")
        time.sleep(3)
        sound.stop()
        os.system('cls||clear')
        time.sleep(1)
        print("Game reset!")
        time.sleep(1)
        os.system('cls||clear')

main()