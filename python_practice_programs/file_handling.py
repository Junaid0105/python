# write the data in practice file
# with open("practice.txt","w") as file:
#     file.write("I am learning java\nI am doing code in java")
#     file.write("\nwhat do you want in java")

# replace java with python in all text
# with open("practice.txt","r") as file:
#     data = file.read()

# new_data = data.replace("java","python")


# with open("practice.txt","w") as file:
#     file.write(new_data)


# with open("practice.txt", "r") as file:
#     da = file.read()
#     print(da)
# word = "Learning"
# with open("practice.txt","r") as file:
#     data = file.read()

# #check wheather the word 'learning' is present or not

# if ("learning" in data):
#     print("YES") 

# def check_word():
#     word = "learning"
#     with open("practice.txt","r") as file:
#         data = file.read()

#         if (word in data):
#             print("found")
#         else:
#             print("not found0")

# check_word()

def check_line():
    line_no = 1
    data = True
    word = "code"
    with open("practice.txt","r") as file:
        while data:

            data = file.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1
    return -1
check_line()