from random import randint

player_score = 0
computer_score = 0
winning_score = 3
while player_score < winning_score and computer_score < winning_score:
    random = randint(1, 3)
    computer = None
    if random == 1:
        computer = "rock"
    elif random == 2:
        computer = "paper"
    else:
        computer = "scissors"
    # print(computer)

    # random2 = randint(1, 3)
    # player = None
    # if random2 == 1:
    #     player = "rock"
    # elif random2 == 2:
    #     player = "paper"
    # else:
    #     player = "scissors"
    # print(player)
    print(f"Player: {player_score}, Computer: {computer_score}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    print("shoot!")
    #computer = input("computer Enter your choice!: ")
    player = input("Player Enter your choice!: ").lower()

    if player == "quit" or player =="q":
        print("Thank you for playing")
        break
    print(f"computer plays: {computer}")
    #if computer != "" and player != "":
    if computer != "" and player != "" and player in 'rps':
        if computer[0] == "r":
            if player[0] == "r":
                print("It is  a Tie")
            elif player[0] == "p":
                print("player Won")
                player_score += 1
            else:
                print("computer Won!")
                computer_score += 1
        elif computer[0] == "p":
            if player[0] == "r":
                print("computer Won")
                computer_score += 1
            elif player[0] == "p":
                print("It is a Tie")
            else:
                print("player Won!")
                player_score += 1
        elif computer[0] == "s":
            if player[0] == "r":
                print("player Won")
                player_score += 1
            elif player[0] == "p":
                print("computer Won")
                computer_score += 1
            else:
                print("It is a Tie!")
    else:
        print("Invalid Input")
        break
#print(type(computer_score))
if player_score > computer_score:
    print(f"Player Won! Final Score {player_score}")
elif player_score < computer_score:
    print(f"Computer Won! Final Score {computer_score}")
elif player_score != 0 and computer_score !=0 and player_score == computer_score:
    print("It is a Tie")