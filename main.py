# This is a sample Python script.
from datetime import datetime

from expense_tracker import ExpenseTracker


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def console_menu():
    print("**********************  Welcome to Expense Tracker! ****************************")
    print("What would you like to do?")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Track budget")
    print("4. Save expenses")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice


def console_enter_monthly_budget():
    ExpenseTracker.monthly_budget = float(input("Enter monthly budget: "))

def console_add_expense():
    print("Enter expense details")
    amount = float(input("Amount: "))
    category = input("Category: ")

    while True:
        date_input = input("Date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    description = input("Description: ")
    return {"amount": amount, "category": category, "date": date_input, "description": description}


def add_expense_to_tracker():
    expense = console_add_expense()
    expense_tracker.add_expense(expense)


def monthly_expense_tracker():
    if ExpenseTracker.monthly_budget == 0:
        console_enter_monthly_budget()
    print("Monthly budget: ", ExpenseTracker.monthly_budget)
    expense_tracker.calculate_total_expenses_recorded()

def view_expenses():
    print("View expenses")
    print("1. View all expenses")
    print("2. View expenses by category")
    print("3. View expenses by month")
    print("4. View expenses by year")
    print("5. View expenses by date range")
    print("6. View expenses by amount range")
    print("7. View expenses by category and month")
    print("8. View expenses by category and year")
    choice = input("Enter your choice: ")
    switcher = {
        '1': expense_tracker.get_view_all_expenses,
        '2': lambda: print("View expenses by category"),
        '3': lambda: print("View expenses by month"),
        '4': lambda: print("View expenses by year"),
        '5': lambda: print("View expenses by date range"),
        '6': lambda: print("View expenses by amount range"),
        '7': lambda: print("View expenses by category and month"),
        '8': lambda: print("View expenses by category and year")
    }
    action = switcher.get(choice, lambda: print("Invalid choice"))
    action()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    expense_tracker = ExpenseTracker()
    while True:
        choice = console_menu()
        print(choice)

        switcher = {
            '1': add_expense_to_tracker,
            '2': view_expenses,
            '3': monthly_expense_tracker,
            '4': lambda: print("Save expenses"),
            '5': lambda: exit()
        }

        action = switcher.get(choice, lambda: print("Invalid choice"))
        action()
