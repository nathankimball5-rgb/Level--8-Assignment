from level8other import BankAccount

print("Welcome to the bank of Nathan")

user_name = input("Please enter your name: ")
user_account = BankAccount(user_name)
user_choice = 0

while user_choice != "4":
    print("You can do any of the following, please select the number to indicate that you want to choose that option.")
    print()
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. quit")
    print()

    user_choice = (input("Please choose an option: " ))

    while user_choice not in ("1", "2", "3", "4"):
        print("Invalid choice, please try again.")
        user_choice = (input("Please choose an option: " ))

        
    if user_choice == "1":
        deposit_amount = float(input("How much would you like to deposit? "))
        try:
            user_account.deposit(deposit_amount)
        except Exception as error:
            print(error)

    elif user_choice == "2":
        withdrawl_amount = float(input("How much would you like to withdraw? "))
        try:
            user_account.withdraw(withdrawl_amount)
        except Exception as error:
            print(error)

    elif user_choice == "3":
        user_account.view_info()


print("Thank you for your business")


