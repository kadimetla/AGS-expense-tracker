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
            print("Date: ", expense["date"])
            print("Amount: ", expense["amount"])
            print("Category: ", expense["category"])
            print("Description: ", expense["description"])

    def calculate_total_expenses_recorded(self):
        total_expenses_recorded = 0
        for index,expense in enumerate(self.expenses):
            if expense["amount"]:
                total_expenses_recorded += expense["amount"]
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

    def get_expenses_by_month(self, month):
        month_expenses = []
        for expense in self.expenses:
            if expense.date.month == month:
                month_expenses.append(expense)
        return month_expenses

    def get_expenses_by_year(self, year):
        year_expenses = []
        for expense in self.expenses:
            if expense.date.year == year:
                year_expenses.append(expense)
        return year_expenses

    def get_expenses_by_date_range(self, start_date, end_date):
        date_range_expenses = []
        for expense in self.expenses:
            if start_date <= expense.date <= end_date:
                date_range_expenses.append(expense)
        return date_range_expenses

    def get_expenses_by_amount_range(self, start_amount, end_amount):
        amount_range_expenses = []
        for expense in self.expenses:
            if start_amount <= expense.amount <= end_amount:
                amount_range_expenses.append(expense)
        return amount_range_expenses

    def get_expenses_by_category_and_month(self, category, month):
        category_month_expenses = []
        for expense in self.expenses:
            if expense.category == category and expense.date.month == month:
                category_month_expenses.append(expense)
        return category_month_expenses

    def get_expenses_by_category_and_year(self, category, year):
        category_year_expenses = []
        for expense in self.expenses:
            if expense.category == category and expense.date.year == year:
                category_year_expenses.append(expense)
        return category_year_expenses

    def get_expenses_by_category_and_date_range(self, category, start_date, end_date):
        category_date_range_expenses = []
        for expense in self.expenses:
            if expense.category == category and start_date <= expense.date <= end_date:
                category_date_range_expenses.append(expense)
