'''
whats your size?
{small : 15
}

{medium : 20}
{large : 25}
do you want pep?
{yes : 
(details:
bill>15
bill + 3
otherwise:
bill+ 2)
}

do you want to have extra cheez?
{y: add $1 to total bill}

'''

size = input('enter your size')
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill +=  20
elif size == 'L':
    bill += 25
pep = input('do you want  pepronie')
if pep == 'y':
    if bill >15:
        bill += 3
    else:
        bill += 2
cheez  = input('do you want extra cheez?')
if cheez =='y':
    bill += 1
print(f'your  final bill is {bill}')


