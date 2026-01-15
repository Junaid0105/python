age = int(input("enter the age: "))
day = input("Enter the day: ")

price = 12 if age > 18 else 8

if day == "Wed":
    price = price - 2

print("The price of movie ticket is ",price)