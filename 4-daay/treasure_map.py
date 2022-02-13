'''
mark a X at the position provided by the user
{Note: the way we nevegate is like first we specifies horizental column number and then  we specifies vertical row like this column 2 and row 3}
thus the first digit will be the place for horizental column
and the second digit will be for vertical row
{
    the first digit is vertical column
the second digit is  the hortizonal row
the above way to nevigate rows is very easy 
}
convert each into integer  seperately
now first use row position then  column position
'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

positionColum = int(position[0])-1
positionRow = int(position[1])-1
map[positionRow][positionColum] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")