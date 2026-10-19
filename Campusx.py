#Oops#

# Oops helps to specify code and write codes in minimum lines#

#---------------------------------------------------------------
#Class is a Blue Print
#---------------------------------------------------------------

#Class : 
# It contains attributes
# It contains Functions


#--------------------------------------------------------------

#Class name Should be in Pascal Case Ex. Car
#Objects case must be in snake Case Ex. wagnor

##syntax to define Obj:
# wagnor=Car()

#---------------------------------------------------------------

#Function : which is not written inside a Class
#Method : which is Written in a Class


#Constructor

class Campusx:

    def __init__(self):

        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
                    hello, How would u like to proceed?
                    1. Enter 1 to creat pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
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
        elif user_input == "5":
            print("Exit")
        else:
            print("Invalid choice ")

    def create_pin(self):
        self.pin = input("Enter Your pin")
        print("Pin set Successfully ")

    def deposit(self):
        temp = input("Enter Your pin")
        if temp == self.pin:
            amt = int(input(" Enter The amount "))
            self.balance = self.balance + amt
            print("Deposit Successfully ")

        else:
            print(" Invalid Pin ")

    def withdraw(self):

        temp = input("Enter Your pin")
        if temp == self.pin:
            amt = int(input(" Enter The amount "))
            if amt <= self.balance:
                self.balance = self.balance - amt
                print(" Operation Successful ")
            else:
                print(" Insufficient Funds ")
        else:
            print(" Invalid Pin ")

    def check_balance(self):
        temp = input("Enter your pin ")
        if temp == self.pin:
            print(self.balance)
        else:
            print(" Invalid Pin")


obj = Campusx()