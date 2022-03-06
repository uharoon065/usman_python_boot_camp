from replit import clear
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
    

calDict= {
    "+":add,
    "-": subtract,
    '*': multiply,
    '/' : divide
}

def calculator():
    ''' performb  simple mathimatical  operations'''
    n1 = float(input('enter a number'))
    for k in calDict:
        print(k,sep='  ,')
    # operation = input('which operation do you want to perform\n')
    is_calculation_continue = False
    while not is_calculation_continue:
        operation = input('which operation do you want to perform\n')
        n2  = float(input('enter the next number'))
        calFunc = calDict[operation]
        answer = calFunc(n1,n2)
        print(f"{n1 }{operation }{n2 }= {answer}")

        calculation_continue = input(f'do you want to continue calculating with value of {answer} ? : y or n\n').lower()
        if calculation_continue == 'n':
            is_calculation_continue = True
            calculator()
        else:
            n1 = answer 

calculator()