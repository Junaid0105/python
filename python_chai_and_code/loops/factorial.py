num = int(input("Enter the number : "))
i = 0
factorial = 1
while i<num:
    factorial = factorial * (num-i)
    i = i+1
print(factorial)
