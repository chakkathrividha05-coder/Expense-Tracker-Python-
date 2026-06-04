expenses = []

def add_expense():
    name = input("Enter Expense Name: ")
    amount = float(input("Enter Expense Amount: ₹"))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense Added Successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("\nNo Expenses Found.")
        return

    print("\n----- Expense List -----")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']}")

def total_expense():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expense: ₹{total}")

def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    try:
        index = int(input("Enter Expense Number to Delete: "))
        expenses.pop(index - 1)
        print("Expense Deleted Successfully!")
    except:
        print("Invalid Selection!")

while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
