# Atm
class Atm:
    def __init__(self):
        self.pin = " "
        self.balance = 0




def menu(self):
    user_input("""
  1. Press 1 to create Pin
  2. Press 2 to change Pin
  3. Press 3 to check Balance
  4. Press 4 to withdraw
  5. Anything else to exit
        """)
    if user_input == "1":
        self.create_pin()
    elif user_input == "2":
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    else:
        exit()

    def create_pin(self):
        user_pin = input("Enter your Pin")
        self.pin = user_pin

        user_balance = int(input("Enter balance"))
        self.balance = user_balance
        print("Pin created successfully")

obj = Atm()
obj.menu()

print(type(obj))