'''
write a program that calculates students height
forbidden : use of methods sum and len
create two variables 
first will keep track of the  number of itterations
the second will add height  on each itteration
everage = sum of students heights/ number of students
round the result at the end
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
counter = 0
sumOfHeights = 0
for h in student_heights:
    sumOfHeights += h
    counter += 1

average = sumOfHeights/counter
print(round(average))



