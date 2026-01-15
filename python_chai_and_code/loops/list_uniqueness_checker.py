list1 = ["mango", "apple", "grapes","apple", "watermelon", "mango"]

unique_element = set()

for i in list1:
    if i in unique_element:
        print("duplicate element is : ", i)
        break
    else:
        unique_element.add(i)
