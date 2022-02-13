#  remember that you can concat the  list  with plus operator 
#  but if you use + you have to concat  asequence 
#  if it is string it will create a  list and concat it  
# butif it is a list it will concat  the elements of it
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#  eassy level
'''
passward = ''
for l in range(nr_letters):
    passward += random.choice(letters)
for s in range(nr_symbols):
    passward += random.choice(symbols)

for n in range(nr_numbers):
    passward += random.choice(numbers)


print(list(passward))
print(f"your passward is {passward}")
'''
# hard level the the passward must not be in the same letter , symbal and number format it should be random
passward = []
for l in range(nr_letters):
    passward.append(random.choice(letters))
for s in range(nr_symbols):
    passward.append(random.choice(symbols))

    
for n in range(nr_numbers):
    passward.append(random.choice(numbers))

shuffledPassward  = ''

print(passward)
random.shuffle(passward)
print(passward)
for c in passward:
    shuffledPassward += c

print(f"your passward is : {shuffledPassward} ")