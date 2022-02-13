'''
welcome to treasure ireland
your at ireland
you are at cross road
chose your distination 
{ left:
you will pass this stage
}
{ on any  other choice you will will fell into a well}
'''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("\n you are at cross road.\n")
choice1 = input('do you wanna go to left or right?\n').lower()
if choice1 != 'left':
    print(" you fell into the well.\n game over")
else:
    print("you have arrived to the lake\n")
    choice2 = input('do you wanna wait or swim?\n').lower()
    if choice2 != 'wait':
        print(" you have been eatten  by a shark.\n game over")
    else:
        print("\n  you have arrived to the  house.\n ")
        choice3 = input(' which door you want to go to? red , blue, or white\n').lower()
        if choice3 == 'white':
            print("congradulation you won the treasure")
        elif choice3 == 'red':
            print(" the fire has burned you alive")
        else:
            print(" you have been eatten by the the wolfes")
