class ExpenseTracker:
    monthly_budget = 0
    def __init__(self):
        self.expenses = []



    def get_expenses(self):
        return self.expenses

    def add_expense(self, expense):
        print(expense)
        self.expenses.append(expense)
        print("Expense added successfully!", self.expenses)

    def get_total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
    def get_view_all_expenses(self):
        for index,expense in enumerate(self.expenses):
            print("Expense #", index + 1)
            print("Date: ", expense["Date"])
            print("Amount: ", expense["Amount"])
            print("Category: ", expense["Category"])
            print("Description: ", expense["Description"])

    def calculate_total_expenses_recorded(self):
        total_expenses_recorded = 0
        for index,expense in enumerate(self.expenses):
            if expense["Amount"]:
                total_expenses_recorded += expense["Amount"]
                if total_expenses_recorded >= ExpenseTracker.monthly_budget:
                    print("You have reached your monthly budget!")
                    break

        print("Total expenses recorded: ", total_expenses_recorded)
        print("Monthly budget: ", ExpenseTracker.monthly_budget , " You have ", ExpenseTracker.monthly_budget - total_expenses_recorded, " left for the month" )


    def get_expenses_by_category(self, category):
        category_expenses = []
        for expense in self.expenses:
            if expense.category == category:
                category_expenses.append(expense)
        return category_expenses

