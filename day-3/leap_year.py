'''
1 a year that is evenly divisible by 4 except  those which are  evenly divisibly by 100

'''

year = int(input('enter the year'))

if year%4==0:
    if year%100 == 0:
        if year%400 != 0:
            print('Not leap year')
        else:
            print(' a leap year')
    else:
        # if year%400 != 0:
            # print('Not leap year')
        # else:
        print(' a leap year')
else:
    print('Not a leap year')

