'''

take two names.
check how many ttimes latters T,R,U,E occurs in both names
check how many times latters L,O,V,E occurs in both names
then add  each of the word true and love occurance respectively
then concat  those two
now cast the concatinated string into a number
conditions for love score
{ 
for     score <10 or score >90
Your score is 125, you go together like coke and mentos.
}
{
    for score  that is > 40 and <50
    "Your score is **y**, you are alright together."
}
{
    otherwise :
    "Your score is **z**."
}
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
trueCount = 0
loveCount = 0

namesCombined = name1 + " " + name2
namesCombined = namesCombined.lower()
for i in 'true':
    trueCount += namesCombined.count(i)
for i in 'love':
    loveCount += namesCombined.count(i)

trueCount = str(trueCount)
loveCount = str(loveCount)
loveScore = int(trueCount + loveCount)
if loveScore< 10 or loveScore> 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore > 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
