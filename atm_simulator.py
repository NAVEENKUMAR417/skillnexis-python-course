balance = 1000


def login():
    correct_pin = "1234"

    while True:
        pin = input("Please enter the PIN: ")

        if pin == correct_pin:
            print("Login successful")
            print("Welcome Customer")
            break
        else:
            print("Login failed")
            print("Please try again")


def check_balance(balance):
    if balance <= 0:
        return "Insufficient balance"
    else:
        return balance


def deposit(balance):
    amount = int(input("Please enter the amount: "))
    balance = balance + amount
    print("Deposited successfully")
    print("new balance: ", balance)
    return balance


def withdraw(balance):
    amount = int(input("Please enter the amount: "))
    balance = balance - amount
    print("Withdrawn successfully")
    print("remaining balance: ", balance)
    return balance

login()

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    operation = input("Enter your choice: ")

    if operation == "1":
        print("Balance:", check_balance(balance))

    elif operation == "2":
        balance = deposit(balance)

    elif operation == "3":
        balance = withdraw(balance)

    elif operation == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")