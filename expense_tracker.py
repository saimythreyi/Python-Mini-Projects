expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nYour Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['category']} - ₹{expense['amount']}")

def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total}")

print("💰 Welcome to the Expense Tracker!")

while True:
    print("\nOptions:")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (Food, Travel, etc.): ")
        add_expense(amount, category)
        print("Expense added successfully!")
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
