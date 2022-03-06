# from replit import clear
#HINT: You can call clear() to clear the output in the console.
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
    # clear()

highest_bidder = {}
highest_bid = 0
for d in option:
    if d['bid'] >    highest_bid :
        highest_bid = d['bid']
        highest_bidder['name'] = d['name']
        highest_bidder['bid'] = highest_bid


print(f"the winner is {highest_bidder['name']} with bid of ${highest_bidder['bid']}")





