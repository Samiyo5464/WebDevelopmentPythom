print("...rock...")
print("...paper...")
print("...scissors...")
print("shoot!")
player_1 = input("Player 1 Enter your choice!: ")
player_2 = input("Player 2 Enter your choice!: ")
if player_1 == player_2 and player_1 != "" and player_2 !="":
    print("It is a tile")
elif player_1 == "rock" and player_2 == "paper":
    print("player 2 won!")
elif player_1 == "rock" and player_2 == "scissors":
    print("player 1 won!")
elif player_1 == "paper" and player_2 == "rock":
    print("player 2 won!")
elif player_1 == "paper" and player_2 == "scissors":
    print("player 2 won!")
elif player_1 == "scissors" and player_2 == "paper":
    print("player 1 won!")
elif player_1 == "scissors" and player_2 == "rock":
    print("player 2 won!")
else:
    print("Invalid Input")