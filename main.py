import random #importing random

while True: #iterate loop
    user_action= input("Enter a choice (Rock, Paper, Scissors): ")#take input
    possible_actions= ["rock","paper","scissors"]
    
    computer_action= random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action== computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action== 'rock':
        if computer_action=='scissors':
            print("Rock smashes scissors, you win!")
        else:
            print("paper covers rock, you lose!")
    elif user_action== 'paper':
        if computer_action=='rock':
            print("paper covers rock, you win!")
        else:
            print("scissors cut paper, you lose!")

    elif user_action== 'scissors':
        if computer_action=='paper':
            print("Scissors cut paper, you win!")
        else:
            print("rock smashes scissors, you lose!")
    #take input for playing again
    play_again= input("Play again? (y/n): ")
    if play_again != "y":
        break