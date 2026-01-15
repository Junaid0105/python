score = int(input("Enter the score"))
if score >= 101:
    print("Invalid score")
    exit()
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"
print("The grade is: ", grade)