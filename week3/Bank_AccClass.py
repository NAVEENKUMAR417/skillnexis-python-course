class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Not enough money")

    def display_balance(self):
        print("Your current balance is:", self.balance)


account = BankAccount(10000)

print("Welcome to the Bank")

while True:
    print("\n## Please select an option ##")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        amount = int(input("Enter deposit amount: "))
        account.deposit(amount)

    elif user_choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif user_choice == 3:
        account.display_balance()

    elif user_choice == 4:
        print("Thank you for using this application!")
        break

    else:
        print("Invalid choice")