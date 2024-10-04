class Atm:
    # Constructor (special function)
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("""Hi, how can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Press 5 to exit
            Your choice: """)
        
        if user_input == '1':
            # Create pin
            self.create_pin()

        elif user_input == "2":
            # Change pin
            self.change_pin()

        elif user_input == "3":
            # Check balance
            self.check_balance()

        elif user_input == "4":
            # Withdraw
            self.withdraw()

        else:
            exit()

    def create_pin(self):
        user_pin = input("Create a pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter balance: "))
        self.balance = user_balance

        print("Pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin changed successfully")
            self.menu()
        else:
            print("Wrong pin")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"Your balance is {self.balance}")
            self.menu()
        else:
            print("You entered the wrong pin")
            self.menu()

    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            # Allow withdrawal
            amount = int(input("Enter amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw successful. The current balance is {self.balance}")
                self.menu()
            else:
                print("You have insufficient balance")
                self.menu()
        else:
            print("Your pin is wrong!")
            self.menu()

# Create an instance of Atm
obj = Atm()
