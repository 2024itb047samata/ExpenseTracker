# Student Expense Tracker

expenses = [
    {"date": "2026-06-01", "amount": 120, "category": "food"},
    {"date": "2026-06-02", "amount": 50, "category": "travel"},
    {"date": "2026-06-03", "amount": 299, "category": "recharge"}
]

monthly_budget = None


def add_expense():
    global expenses

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input(
        "Enter category (food/travel/recharge/other): "
    ).lower()

    if category not in ["food", "travel", "recharge", "other"]:
        category = "other"

    expenses.append({
        "date": date,
        "amount": amount,
        "category": category
    })

    print("Expense added successfully!")

    check_budget()


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- ALL EXPENSES -----")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. Date: {expense['date']} | "
            f"Amount: Rs. {expense['amount']} | "
            f"Category: {expense['category']}"
        )


def total_spent():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Amount Spent: Rs. {total}")


def highest_spending_category():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    highest_category = max(category_totals, key=category_totals.get)

    print(f"\nHighest Spending Category: {highest_category}")
    print(f"Amount Spent: Rs. {category_totals[highest_category]}")


def set_budget():
    global monthly_budget

    try:
        monthly_budget = float(input("Enter monthly budget: "))
        print("Budget set successfully!")
        check_budget()

    except ValueError:
        print("Invalid budget amount!")


def check_budget():
    if monthly_budget is None:
        return

    total = sum(expense["amount"] for expense in expenses)

    if total > monthly_budget:
        print(
            f"WARNING: Budget exceeded by Rs. "
            f"{total - monthly_budget:.2f}"
        )
    else:
        print(
            f"Remaining Budget: Rs. "
            f"{monthly_budget - total:.2f}"
        )


def main():
    while True:
        print("\n==============================")
        print("   STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Amount Spent")
        print("4. Highest Spending Category")
        print("5. Set Monthly Budget")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_spent()

        elif choice == "4":
            highest_spending_category()

        elif choice == "5":
            set_budget()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()