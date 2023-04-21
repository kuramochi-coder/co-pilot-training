# Write a rock, paper, scissors, lizard, spock game
# import the random module
import random


# define main function that handles all the logic
def main():
    # define a list of choices
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    # define a dictionary of outcomes
    outcomes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"],
    }

    # get the user's choice
    user_choice = input("Enter your choice: ")

    # get the computer's choice
    computer_choice = random.choice(choices)

    # print the user's choice
    print("You chose", user_choice)
    # print the computer's choice
    print("Computer chose", computer_choice)

    # if the user's choice is in the outcomes dictionary
    if user_choice in outcomes:
        # if the computer's choice is in the outcomes dictionary
        if computer_choice in outcomes:
            # if the computer's choice is in the outcomes list
            if computer_choice in outcomes[user_choice]:
                # print the user wins message
                print("You win!")
            # if the user's choice is in the outcomes list
            elif user_choice in outcomes[computer_choice]:
                # print the computer wins message
                print("Computer wins!")
            # otherwise
            else:
                # print the tie message
                print("Tie!")
        # otherwise
        else:
            # print the error message
            print("Error: Computer choice is not in outcomes dictionary")
    # otherwise
    else:
        # print the error message
        print("Error: User choice is not in outcomes dictionary")


# game starts here
def game(user_choice, computer_choice):
    # define a dictionary of outcomes
    outcomes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"],
    }

    # print the user's choice
    print("You chose", user_choice)
    # print the computer's choice
    print("Computer chose", computer_choice)

    # if the user's choice is in the outcomes dictionary
    if user_choice in outcomes:
        # if the computer's choice is in the outcomes dictionary
        if computer_choice in outcomes:
            # if the computer's choice is in the outcomes list
            if computer_choice in outcomes[user_choice]:
                # print the user wins message
                print("You win!")
                return "You win!"
            # if the user's choice is in the outcomes list
            elif user_choice in outcomes[computer_choice]:
                # print the computer wins message
                print("Computer wins!")
                return "Computer wins!"
            # otherwise
            else:
                # print the tie message
                print("Tie!")
                return "Tie!"
        # otherwise
        else:
            # print the error message
            print("Error: Computer choice is not in outcomes dictionary")
    # otherwise
    else:
        # print the error message
        print("Error: User choice is not in outcomes dictionary")


# call the main function
if __name__ == "__main__":
    main()
