
# ATM Class using Object-Oriented Programming in Python

class ATM:
    def __init__(self):
        # Initialize balance and default PIN
        self.balance = 1000
        self.pin = "1234"
        self.is_authenticated = False  # Track if the user has entered the correct PIN

    def check_pin(self, input_pin):
        # Check if entered PIN matches the stored PIN
        if input_pin == self.pin:
            self.is_authenticated = True
            print("PIN verified successfully.\n")
        else:
            self.is_authenticated = False
            print("Incorrect PIN.\n")

    def check_balance(self):
        # Display current balance if authenticated
        if self.is_authenticated:
            print(f"Your current balance is: Rs. {self.balance}\n")
        else:
            print("Access denied. Please enter correct PIN first.\n")

    def deposit(self, amount):
        # Deposit amount if authenticated and valid
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f"Successfully deposited Rs. {amount}.")
                print(f"New balance: Rs. {self.balance}\n")
            else:
                print("Invalid deposit amount. Must be greater than 0.\n")
        else:
            print("Access denied. Please enter correct PIN first.\n")

    def withdraw(self, amount):
        # Withdraw amount if authenticated and valid
        if self.is_authenticated:
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Successfully withdrew Rs. {amount}.")
                    print(f"New balance: Rs. {self.balance}\n")
                else:
                    print("Insufficient balance.\n")
            else:
                print("Invalid withdrawal amount. Must be greater than 0.\n")
        else:
            print("Access denied. Please enter correct PIN first.\n")

    def exit(self):
        # Exit the ATM
        print("Thank you for using the ATM. Goodbye!\n")


# Menu-based system
def run_atm():
    atm = ATM()
    print("Welcome to ATM")

    # Ask user to enter PIN once at the beginning
    entered_pin = input("Please enter your PIN: ")
    atm.check_pin(entered_pin)

    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.\n")
        elif choice == '4':
            atm.exit()
            break
        else:
            print("Invalid choice. Please select from 1 to 4.\n")


# Run the program
run_atm()
