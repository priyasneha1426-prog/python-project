
class ExpenseTracker:

    def __init__(self, name, currency):
        self.name = name
        self.currency = currency
        self.income_amount = 0
        self.total_expense = 0
        self.investment = 0

    def income(self):
        income = int(input("Enter the total income: "))
        addin = int(input("Enter extra income if there: "))

        self.income_amount = income + addin

        print("Total income:", self.currency, self.income_amount)

    def expense(self):
        food = int(input("Enter the expense on food: "))
        travel = int(input("Enter the expense on travel: "))
        shopping = int(input("Enter the expense on shopping: "))
        others = int(input("Enter the expense on others: "))

        self.total_expense = food + travel + shopping + others

        print("Total expense:", self.currency, self.total_expense)

    def invest(self):
        self.investment = int(input("Enter the amount invested: "))

        print("Total investment:", self.currency, self.investment)

    def savings(self):
        save = self.income_amount - self.total_expense - self.investment

        print("Total savings:", self.currency, save)

obj = ExpenseTracker("abc", "INR")

print("Welcome", obj.name)

obj.income()
obj.expense()
obj.invest()
obj.savings()
