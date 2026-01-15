class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.menu()
    def menu(self):
        user_input = input("""
                            Hello, How would like to proceed
                            1. Enter 1 to create pin
                            2. Enter 2 to deposit
                            3. Enter 3 to withdraw
                            4. Enter 4. to check balance
                            5. Enter 5 to exit
                            """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
    ## Getter and setter method-----------        
    def get_pin(self):
        return self.__pin
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed")
    ##------------------------------------
    def create_pin(self):
        self.__pin = input("Enter the pin")
        print("pin set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter the pin")
        if temp == self.__pin:
            amount = int(input("Enter the deposit amount"))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
        #self.menu()

    def withdraw(self):
        temp = input("Enter the pin")
        if temp == self.__pin:
            amount = int(input("Enter the withdraw amount"))
            if amount<self.__balance:
                self.__balance = self.__balance - amount
                print("transaction successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
        #self.menu()
    def check_balance(self):
        temp = input("Enter pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")
    
            
