'''
i have a list of numbers  ive to find hightest one
first  i think i have to compare the first number to see if it is equal to or greater then rest of elements
to do that i think i will use nested loop to track the first  element and in the secod loop i will compare it to all the elements
78 65 89 86 55 91 64 89
is 78 > 78
no  hs = 78
is 78 >  89
no hs = 89
is 78 >  86 
no hs = 86
is 78 >  55
 yes  hs = 78
 is 78 > 91
 no hs =  91
 is 78 > 89
 no hs = 89

'''
# 🚨 Don't change the code below 👇


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
hightestScore = 0
for s in student_scores:
    score = s
    for c in student_scores:
        # print(c)
        if score > c:
            hightestScore = score
        elif score < c:
            hightestScore = c

print(hightestScore)




