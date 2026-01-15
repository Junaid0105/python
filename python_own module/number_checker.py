#check number is even or odd
def is_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")


# check wheather the number is prime or not
def is_prime(num):
    if num<=1:
        return "No prime"
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return "No prime"
    return "No prime"


# find factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)