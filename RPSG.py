import random   #imports random module(file with code) which has random number generation related functions
"""
Project Workflow: 
1. Take user input
2. computer input is random
3. display result 


"""
options = ("rock", "paper", "scissor")
playing = True

while playing:  # a loop to run the game again

    #now after every new game the input is reset
    player = None
    computer = random.choice(options)


    while player not in options:    #if the player doesnt choose any of the options the while loop runs forever but if options chosen loop is escaped
        player = input("Enter  a choice(rock, paper, scissor): ")

    print(f"Player :{player}")  #embedding expressions inside string literal using {} for readable
    print(f"Computer :{computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose")

    if not input("Do you want to play again? (y/n): ").lower() == "y":
        playing = False

print("Thank you for Playing!!!!")


    