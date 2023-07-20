import random
exit = False
user_points = 0
computer_points =  0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock,paper,scissors or exit ")
    computer_input = random.choice(options)

    if user_input == "exit" : 
        print("Game ended.")
        print("You won a total score of "+str(user_points) +" and the total computer score is "+str(computer_points))
        exit == True
        quit()

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock.")
            print("Computer input is also rock.")
            print("It is a tie :) ")
        elif computer_input == "paper":
            print("Your input is rock.")
            print("Computer input is paper.")
            print("Computer wins! Try again maybe luck will be on your side.")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock.")
            print("Computer input is scissors.")
            print("You win,congrats!")
            user_points += 1
        else:
            print("Invalid option.")
    if user_input == "paper":
        if computer_input == "paper":
            print("Your input is paper.")
            print("Computer input is also paper.")
            print("It is a tie :) ")
        elif computer_input == "rock":
            print("Your input is paper.")
            print("Computer input is rock.")
            print("You win,congrats!")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is paper.")
            print("Computer input is scissors")
            print("Computer wins! Try again maybe luck will be on your side.")
            computer_points += 1
        else:
            print("Invalid option.")
        if user_input == "scissors":
            if computer_input == "scissors":
                print("Your input is scissors.")
                print("Computer input is also scissors.")
                print("It is a tie :) ")
            elif computer_input == "rock":
                print("Your input is scissors.")
                print("Computer input is rock.")
                print("Computer wins! Try again maybe luck will be on your side.")
                computer_points += 1
            elif computer_input == "paper":
                print("Your input is scissors.")
                print("Computer input is paper.")
                print("You win,congrats!")
                user_points += 1
            else:
                print("Invalid option.")