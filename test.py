import random

def welcome():
    print("Welcome to rock, paper, scissors! ")
    print("To exit type 'exit'")

def pick_move():
    moves = ["Rock", "Paper", "Scissors"]
    choice = random.choice(moves)
    print(choice)
    return (choice)
    

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

def winner(choice, user_choice):
    

def main():
    while True:
        welcome()
        choice = pick_move()
        user_choice = user_move()
        if user_choice == "exit":
                return
        winner(choice, user_choice)

main()