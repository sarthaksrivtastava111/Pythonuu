name = input("Enter your name: ")
balance = 0.0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        print(f"{name}, your balance is ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
        else:
            print("Enter a positive amount.")

    elif choice == "3":
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > balance:
            print("Not enough balance!")
        else:
            balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")