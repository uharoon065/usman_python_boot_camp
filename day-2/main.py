print("welcome to the tip calculator !! \n")
bill = input('what was the total bill? \n')
bill = float(bill)
percentage = float(input('what percentage tip do you want to pay?\n'))/100
persons = input('how many  persons do you want to split bill with?\n')
persons = int(persons)
total = percentage*bill+bill
print(f"each of you have to pay $ {round(total/persons,2)} ")