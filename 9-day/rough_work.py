'''

so first of all i need two inputs and store there values somewhere 
name and bid
now im creating a list to store dicts
after im creating  function to store  dicts in list
now im putting the function in while loop 
secondof all i notice  the program continue untill no bidder is left
i use while loop to check if  any bidder is left or not



'''

option = []
def theHightestBidder(name , bid):
    option.append({ 'name' : name , 'bid' : bid})
isBidingEnds  =False
while not isBidingEnds:
    name = input('what is  your name ? :\n')
    bid = int(input('what is your bid? : \n$'))
    theHightestBidder(name = name , bid = bid)
    bidder= input('is ther any one left to bid?').lower()
    if bidder == 'no':
        isBidingEnds = True

# print(option)
highest_bidder = {}
highest_bid = 0
for d in option:
    if d['bid'] >    highest_bid :
        highest_bid = d['bid']
        highest_bidder['name'] = d['name']
        highest_bidder['bid'] = highest_bid


print(f"the winner is {highest_bidder['name']} with bid of ${}")


#Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    f"Result: {formated_f_name} {formated_l_name}"


#Storing output in a variable
formatted_name = format_name(input("Your first name: "),
                             input("Your last name: "))
print(formatted_name)
#or printing output directly
print(
    format_name(input("What is your first name? "),
                input("What is your last name? ")))

#Already used functions with outputs.
length = len(formatted_name)


#Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it 
  to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"



