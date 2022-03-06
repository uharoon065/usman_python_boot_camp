# prime number those which are only divisible  by itself or 1
def prime_checker(number):
    if number%2 == 0 or number%3 == 0  or number %5 == 0:
        print("its's not a prime number.")
    else:
        print("its's a prime number.")

#  solution of instructor
def prime_checker2(number):
    isPrime = True
    for n in range(2,number):
        if number%n == 0:
            isPrime = False
    if isPrime:
        print("its a prime number")
    else:
        print("not a prime number")


while True:
    number = int(input('enter a number'))
    # prime_checker(number)
    prime_checker2(number)