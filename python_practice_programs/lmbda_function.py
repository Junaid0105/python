
# # check wheather number is positive, negative or zero
# n = lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"

# print(n(4))
# print(n(-3))
# print(n(0))

# # check wheather the number is even or odd using lambda function
# num = lambda x:"Even" if x%2==0 else "Odd"

# print(num(13))
# print(num(12))

# using list

li = [lambda arg=x: arg*10 for x in range(1,6)]

for i in li:
    print(i())