from random import randint
random = randint(1,3)
computer = None
if random == 1:
    computer = "rock"
elif random == 2:
    computer = "paper"
else:
    computer = "scissors"

print("...rock...")
print("...paper...")
print("...scissors...")
print("shoot!")
#computer = input("computer Enter your choice!: ")
print(f"computer plays: {computer}")
player_2 = input("Player 2 Enter your choice!: ").lower()
if computer != "" and player_2 != "":
    if computer[0] == "r":
        if player_2[0] == "r":
            print("It is  a Tie")
        elif player_2[0] == "p":
            print("player 2 Won")
        else:
            print("computer Won!")
    elif computer[0] == "p":
        if player_2[0] == "r":
            print("computer Won")
        elif player_2[0] == "p":
            print("It is a Tie")
        else:
            print("player 2 Won!")
    elif computer[0] == "s":
        if player_2[0] == "r":
            print("player 2 Won")
        elif player_2[0] == "p":
            print("computer Won")
        else:
            print("It is a Tie!")
else:
    print("Invalid Input")