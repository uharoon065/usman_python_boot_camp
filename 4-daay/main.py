from random import choice



#Write your code below this line 👇
rock = "R"
paper = "P"
scissors = "S"
#refactoring the code
'''
player = input("what do you want to chose? 0 , 1 , 2")
# first  you have to change the variable according to the input of the player
if player == '0':
    player = rock
elif player == '1':
    player = paper
else:
    player = scissors
'''
playerChoice = int(input("what do you want to chose? 0 , 1 , 2"))
player = [rock ,paper,scissors]
computerChoice = choice([rock,paper,scissors])
print(f" computer : {computerChoice}")
if playerChoice > 2 or playerChoice<0:
    print("you lose because you have put a invalid entery")
else:
    player = player[playerChoice]
    print(f"player  : {player}")
    if player == computerChoice:
        print("its a draw")
    elif player == rock:
        if computerChoice == paper:
            print(" you lose")
        elif computerChoice == scissors:
            print("you won")
    elif player== paper:
        if computerChoice == rock:
            print("you won")
        elif computerChoice ==scissors:
            print("you lose")
    else:
        if computerChoice == rock:
            print("you lose")
        elif computerChoice == paper:
            print("you won")