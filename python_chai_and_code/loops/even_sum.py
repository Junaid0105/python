number = int(input("enter the number"))
sum = 0
for i in range(1,number+1):
    print(i)
    if i%2 == 0:
        sum = sum + i
print("The sum of even numbers", sum)