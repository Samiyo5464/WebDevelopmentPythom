# print("...rock...")
# print("...paper...")
# print("...scissors...")
# print("shoot!")
# player_1 = input("Player 1 Enter your choice!: ")
# player_2 = input("Player 2 Enter your choice!: ")
# if player_1 and player_2:
#     if player_1 == "rock":
#         if player_2 == "rock":
#             print("It is  a Tie")
#         elif player_2 == "paper":
#             print("player 2 Won")
#         else:
#             print("player 1 Won!")
#     elif player_1 == "paper":
#         if player_2 == "rock":
#             print("player 1 Won")
#         elif player_2 == "paper":
#             print("It is a Tie")
#         else:
#             print("player 2 Won!")
#     elif player_1 == "scissors":
#         if player_2 == "rock":
#             print("player 2 Won")
#         elif player_2 == "paper":
#             print("player 1 Won")
#         else:
#             print("It is a Tie!")
# else:
#     print("Invalid Input")
#
# print("#"*250)
print("...rock...")
print("...paper...")
print("...scissors...")
print("shoot!")
player_1 = input("Player 1 Enter your choice!: ")
player_2 = input("Player 2 Enter your choice!: ")
if player_1 != "" and player_2 != "":
    if player_1[0] == "r":
        if player_2[0] == "r":
            print("It is  a Tie")
        elif player_2[0] == "p":
            print("player 2 Won")
        else:
            print("player 1 Won!")
    elif player_1[0] == "p":
        if player_2[0] == "r":
            print("player 1 Won")
        elif player_2[0] == "p":
            print("It is a Tie")
        else:
            print("player 2 Won!")
    elif player_1[0] == "s":
        if player_2[0] == "r":
            print("player 2 Won")
        elif player_2[0] == "p":
            print("player 1 Won")
        else:
            print("It is a Tie!")
else:
    print("Invalid Input")