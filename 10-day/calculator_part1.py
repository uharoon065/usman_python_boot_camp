
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
    

calculator  = {
    "+":add,
    "-": subtract,
    '*': multiply,
    '/' : divide
}

n1 = float(input('enter a number'))
for k in calculator:
    print(k,sep='  ,')
operation = input('which operation do you want to perform\n')
n2 = int(input('enter a 2nd number'))
calFunc = calculator[operation]
answer = calFunc(n1,n2)
print(f"{n1 }{operation }{n2 }= {answer}")

operation = input('which operation do you want to perform\n')
n2  = int(input('enter the next number'))
calFunc = calculator[operation]
print(f"{answer}{operation }{n2 }= {calFunc(answer,n2)}")
