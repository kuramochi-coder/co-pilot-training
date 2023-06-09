""" main module for the mini game """
# Write a rock, paper, scissors, lizard, spock game
# import the random module
import random


# define main function that handles all the logic
def main():
    """main function that handles all the logic."""
    # define a list of choices
    choices = ["rock", "paper", "scissors", "lizard", "spock"]

    # get the user's choice based on optons.
    print("Enter your choice: ")
    print("1. rock")
    print("2. paper")
    print("3. scissors")
    print("4. lizard")
    print("5. spock")

    # get the user's choice
    user_choice = input("Enter your choice: ")

    # if the user's choice is 1
    final_user_choice = choices[int(user_choice) - 1]

    # get the computer's choice
    computer_choice = random.choice(choices)

    # call the determine_outcome function
    return determine_outcome(final_user_choice, computer_choice)


# game starts here
def determine_outcome(user_choice, computer_choice):
    """determine the outcome of the game"""
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
            return "Error: Computer choice is not in outcomes dictionary"
    # otherwise
    else:
        # print the error message
        print("Error: User choice is not in outcomes dictionary")
        return "Error: User choice is not in outcomes dictionary"


# call the main function
if __name__ == "__main__":
    main()
