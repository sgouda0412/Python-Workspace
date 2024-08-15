class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Thank you, {self.age} year old, {self.name.title()}"


class Bank(User):
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def show_info(self):
        return f"{self.name} has a remaining balance of: £{self.balance}"

    def deposit(self):
        dp = float(input("Please enter how much you would like to input: "))
        print("Thank you for depositing...")
        self.balance += dp
        self.total_deposits += 1
        return f"Your balance is now: £{round(self.balance, 2)}"

    def withdraw(self):
        wd = float(input("Please enter how much you would like to withdraw: "))
        print("Thank you for withdrawing...")
        self.balance -= wd
        self.total_withdraws += 1
        return f"Your balance is now: £{round(self.balance, 2)}"


def options(user_two):
    print("Thank you for creating your Bank account!")
    print(
        "Here are a list of options, please choose a number for the option "
        "you want: "
    )
    while True:
        option_choice = int(
            input(
                "1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total "
                "Withdraws\n5) See Total Deposits\n6) Quit\n"
            )
        )
        if option_choice == 1:
            print(user_one_bank.show_info())
            if option_choice == 1 and user_two is not None:
                print(user_two_bank.show_info())
        elif option_choice == 2:
            print(user_one_bank.withdraw())
            if option_choice == 2 and user_two is not None:
                print(user_two_bank.withdraw())
        elif option_choice == 3:
            print(user_one_bank.deposit())
            if option_choice == 3 and user_two is not None:
                print(user_two_bank.deposit())
        elif option_choice == 4:
            print(f"There have been {user_one_bank.total_withdraws} withdraws")
            if option_choice == 4 and user_two is not None:
                print(f"There have been {user_two_bank.total_withdraws} withdraws")
        elif option_choice == 5:
            print(f"There have been {user_one_bank.total_deposits} deposits")
            if option_choice == 5 and user_two is not None:
                print(f"There have been {user_two_bank.total_deposits} deposits")
        elif option_choice == 6:
            print("Thank you for using your bank. Please come again soon.")
            return False
            break
        else:
            print("Please choose a correct number from 1-7")


def bank_creation():
    balance = float(input("how much money do you have: "))
    return balance


while True:
    print("Welcome to the BC Bank")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    user_one = User(name, age)
    user_two = None
    new_user = input(
        "Would you like to register a new person? Type 'No' to create your " "bank: "
    )
    if new_user.lower() == "yes":
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        user_two = User(name, age)
        print(
            "Thank you for registering 2 people. Please create your bank " "accounts."
        )
        user_one_balance = bank_creation()
        user_two_balance = bank_creation()
        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
        user_two_bank = Bank(user_two.name, user_two.age, user_two_balance)
        flag = options(user_two)
        if not flag:
            break
    else:
        user_one_balance = bank_creation()
        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
        flag = options(user_two)
        if not flag:
            break
