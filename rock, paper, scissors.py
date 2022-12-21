import random

name = input("Enter your name: ")
# Invite the user to enter their name to personalise the game

# create a list of possible choices
choices = ["rock", "paper", "scissors"]

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}")
# create a while loop instead of just an if statement to prevent the user from progressing without entering their name.

while True:

# have the player pick a random choice from the list of choices and print it
    player = input(f"Choose your weapon. Rock, Paper or Scissors?: ").lower()

    play_again_options = ["yes", "no"]

# while loop to handle the situation where the player's choice is not one of the available options
    while player not in choices:
        print("Please select from one of the options available.")
        player = input(
            f"Choose your weapon. Rock, Paper or Scissors?: ").lower()
    else:
        print(f"{name}'s weapon: " + player)

# have the computer pick a random choice from the list of choices and print it
    computer = random.choice(choices)
    print("Computer's weapon: " + computer)

# coding the win conditions
    if player == computer:
        print("Real recognise real. It is a draw.")
    elif player == "rock":
        if computer == "scissors":
            print("Your scissors crushed the computer's rock. You win")
        if computer == "paper":
            print("Your rock got wrapped up by the computer's paper. You lose")
    elif player == "paper":
        if computer == "rock":
            print("You wrapped up the computer's rock. You win")
        if computer == "scissors":
            print("The computer's scissors sliced your ass up. You lose")
    elif player == "scissors":
        if computer == "rock":
            print("The computer's rock crushed up your paper. You lose.")
        if computer == "paper":
            print("You cut up the computer's paper. You win.")
      # if computer choice is rock and user choice is paper - user wins.
      # if computer choice is rock and user choice is rock - it is a draw and you go again.
      # if computer choice is rock and user choice is scissors - computer wins

# asking the player if they want to play again, ina  while loop
    play_again = input("Do you want to play again? (yes/no)").lower()
    while play_again not in play_again_options:
        print("Please choose yes or no")
        play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again == "no":
        print("You do not want to play anymore.")
        break
print("Goodbye")
