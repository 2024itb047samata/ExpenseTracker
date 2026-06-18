# Student Expense Tracker

A simple Python Command Line Interface (CLI) application that helps students track their daily expenses, monitor spending habits, and manage monthly budgets.

## Overview

College students often spend money on food, travel, mobile recharges, and other daily expenses without keeping track of where their money goes. This project provides a lightweight offline solution that allows users to record and analyze expenses directly from the terminal without requiring any internet connection or database.

## Features

* Add new expenses with date, amount, and category
* View all recorded expenses
* Calculate total amount spent
* Identify the highest spending category
* Set a monthly budget
* Receive warnings when spending exceeds the budget
* Works completely offline
* Includes sample expense data for testing

## Technologies Used

* Python 3
* Python Standard Library

## Project Structure

```
Student-Expense-Tracker/
│
├── main.py
├── README.md
└── poster.png
```

## Categories Supported

* Food
* Travel
* Recharge
* Other

## Sample Data

The application comes with preloaded sample expenses:

| Date       | Amount | Category |
| ---------- | ------ | -------- |
| 2026-06-01 | 120    | Food     |
| 2026-06-02 | 50     | Travel   |
| 2026-06-03 | 299    | Recharge |

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## Menu Options

```
1. Add Expense
2. View Expenses
3. Total Amount Spent
4. Highest Spending Category
5. Set Monthly Budget
6. Exit
```

## Example Output

```
==============================
   STUDENT EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Total Amount Spent
4. Highest Spending Category
5. Set Monthly Budget
6. Exit

Enter your choice: 3

Total Amount Spent: Rs. 469
```

## Future Improvements

* Store data in CSV/JSON files
* Generate monthly reports
* Add expense filtering by category
* Create charts and visual analytics
* Build a GUI version using Tkinter
* Cloud synchronization support

## Problem Statement

Students often lose track of small daily expenses such as food purchases, transportation costs, and mobile recharges. Existing solutions are usually mobile applications that require installation and internet connectivity. This project aims to provide a simple, lightweight, and offline expense tracking solution through a command-line interface.

## Conclusion

Student Expense Tracker is a beginner-friendly Python project that demonstrates the use of lists, dictionaries, functions, loops, and user input handling while solving a practical real-world problem. It enables students to manage finances more effectively and develop better spending habits.

---

Developed using Python
