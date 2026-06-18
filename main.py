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
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
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

def category_report():
    if not expenses:
        print("No expenses found.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    total_spending = sum(totals.values())

    print("\n----- CATEGORY REPORT -----")

    for category, amount in totals.items():
        percentage = (amount / total_spending) * 100
        print(f"{category:<10} Rs.{amount:.2f} ({percentage:.1f}%)")

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

def daily_average():
    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    unique_days = set()

    for expense in expenses:
        unique_days.add(expense["date"])

    average = total / len(unique_days)

    print(f"\nAverage Daily Spending: Rs. {average:.2f}")

def largest_expense():
    if not expenses:
        print("No expenses found.")
        return

    largest = max(expenses, key=lambda x: x["amount"])

    print("\n----- LARGEST EXPENSE -----")
    print(f"Date     : {largest['date']}")
    print(f"Amount   : Rs. {largest['amount']}")
    print(f"Category : {largest['category']}")


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
        
def financial_insights():
    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)
    average = total / len(expenses)

    largest = max(expenses, key=lambda x: x["amount"])

    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    top_category = max(totals, key=totals.get)

    print("\n----- FINANCIAL INSIGHTS -----")
    print(f"Total Expenses      : {len(expenses)}")
    print(f"Total Spending      : Rs. {total:.2f}")
    print(f"Average Expense     : Rs. {average:.2f}")
    print(f"Largest Expense     : Rs. {largest['amount']:.2f}")
    print(f"Top Category        : {top_category}")

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
        print("6. Category Report")
        print("7. Daily Average Spending")
        print("8. Largest Expense")
        print("9. Financial Insights")
        print("10. Exit")

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
            category_report()

        elif choice == "7":
            daily_average()

        elif choice == "8":
            largest_expense()

        elif choice == "9":
            financial_insights()

        elif choice == "10":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
