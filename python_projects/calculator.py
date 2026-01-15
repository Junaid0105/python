def addition(number1, number2):
    return number1 + number2
def subtraction(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1 * number2
def divide(number1, number2):
    return number1 / number2
while True:
    print("\n----Calulator----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter the choice: ")
    if choice in ['1','2','3','4']:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))

    match choice:
        case '1':
            print(addition(number1,number2))
        case '2':
            print(subtraction(number1,number2))
        case '3':
            print(multiply(number1,number2))
        case '4':
            print(divide(number1,number2))
        case '5':
            break
        case _:
            print("Invalid choice")