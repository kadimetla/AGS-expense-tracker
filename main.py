# This is a sample Python script.
import csv
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
    return {"Amount": amount, "Category": category, "Date": date_input, "Description": description}


def add_expense_to_tracker():
    expense = console_add_expense()
    expense_tracker.add_expense(expense)

def save_expenses_to_csv(filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for expense in expense_tracker.get_expenses():
            writer.writerow([expense['Date'], expense['Category'], expense['Amount'], expense['Description']])

def load_expenses_from_csv(filename='expenses.csv'):
    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                row['Amount'] = float(row['Amount'])
                expenses.append(row)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty expense tracker.")
    return expenses

def monthly_expense_tracker():
    if ExpenseTracker.monthly_budget == 0:
        console_enter_monthly_budget()
    print("Monthly budget: ", ExpenseTracker.monthly_budget)
    expense_tracker.calculate_total_expenses_recorded()

def view_expenses():
    print("*** View expenses ***")
    print("1. View all expenses")

    choice = input("Enter your choice: ")
    switcher = {
        '1': expense_tracker.get_view_all_expenses,
    }
    action = switcher.get(choice, lambda: print("Invalid choice"))
    action()

def save_and_exit():
    save_expenses_to_csv()
    exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    expense_tracker = ExpenseTracker()
    expense_tracker.expenses = load_expenses_from_csv()
    while True:
        choice = console_menu()
        print(choice)

        switcher = {
            '1': add_expense_to_tracker,
            '2': view_expenses,
            '3': monthly_expense_tracker,
            '4': save_expenses_to_csv,
            '5': save_and_exit
        }

        action = switcher.get(choice, lambda: print("Invalid choice"))
        action()
