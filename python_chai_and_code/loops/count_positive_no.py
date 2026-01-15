list1 = [1,3,2,-9,8,-6]
positive_no = 0
negative_no = 0
for i in list1:
    if i > 0:
        # print("positive numbers",list1[i])
        positive_no = positive_no + 1
    else:
        # print("Negative numbers",list1[i])
        negative_no = negative_no + 1
print("Positive number: ", positive_no, "Negative number: ", negative_no)
