import csv


class Category:
    def __init__(self, category=""):
        self._category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if category == "":
            return None
        self._category = category
        return self._category

    def __str__(self):
        return f"{self._category.strip().capitalize()}"


class Expense:
    def __init__(self, amount=0, category="", date="", description=""):
        self._amount = amount
        self._category = Category(category)
        self._date = date
        self._description = description

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount=0):
        if amount <= 0:
            return None
        self._amount = amount
        return self._amount

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category=""):
        if category == "":
            return None
        self._category = Category(category)
        return self._category

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date=""):
        if date == "":
            return None
        self._date = date
        return self._date

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description=""):
        if description == "":
            return None
        self._description = description
        return self._description

    def __str__(self):
        return f"Amount: ${self._amount}\nCategory: {self._category}\nDate: {self._date}\nDescription: {self._description}"


def add_expense(Expenses, id, amount, category, date, description):
    if id in Expenses:
        return "Id not unique"
    try:
        expense = Expense(amount, category, date, description)
        Expenses[id] = expense
        return "Done"
    except:
        return "Something went Wrong"


def generate_report(
    Expenses,
):
    report = []
    for id in Expenses.keys():
        report.append(id)
    return report


def edit_expense(Expenses, id, amount=0, category="", date="", description=""):
    if id in Expenses:
        expense = Expenses[id]

        try:

            if amount != 0:
                expense.amount = amount
            if category != "":
                expense.category = category
            if date != "":
                expense.date = date
            if description != "":
                expense.description = description
            Expenses[id] = expense
            return "Done"
        except Exception as er:
            return er
    else:
        return "No such Id"


def delete_expense(Expenses, id):
    if id in Expenses:
        Expenses.pop(id)
        return "Done"
    else:
        return "No such Id"


def writer(Expenses):
    with open("./Expense.csv", "w") as file:
        writer = csv.writer(file)
        for key, value in Expenses.items():
            writer.writerow(
                [
                    key,
                    value.amount,
                    value.category.category,
                    value.date,
                    value.description,
                ]
            )


def reader(Expenses):
    try:
        with open("./Expense.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                id = int(row[0])
                amount = int(row[1])
                category = row[2]
                date = row[3]
                description = row[4]
                Expenses[id] = Expense(amount, category, date, description)
    except FileNotFoundError:
        with open("./Expense.csv", "w") as file:
            pass


def menu():
    choice = 0
    print(
        "(1)Add Expense\n(2)Generate Report\n(3)Edit Expense\n(4)Delete Expense\n(-1)To Exit"
    )
    try:
        choice = int(input("Choice: "))
    except ValueError:
        return 0
    return choice


def main():
    Expenses = {}
    reader(
        Expenses,
    )
    while True:
        choice = menu()
        if choice == 1:
            while True:
                try:
                    id = int(input("Unique Expense ID: "))
                    break
                except ValueError:
                    print("Invalid Id")
            while True:
                try:
                    amount = int(input("Input Expense Amount: "))
                    if amount < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid Amount")

            category = input("Input Expense Category: ")
            date = input("Input Date of the Expense: ")
            description = input("Input Description of the Expense: ")
            print(add_expense(Expenses, id, amount, category, date, description))
            writer(
                Expenses,
            )
        elif choice == 2:
            expenses = generate_report(Expenses)
            for expense in expenses:
                print(str(expense) + "\n" + str(Expenses[expense]))
        elif choice == 3:
            id = int(input("Enter Id: "))
            print("Edit:\n(1)Amount\n(2)Category\n(3)Date\n(4)Description\n")
            choice = int(input("Choice: "))
            if choice == 1:
                amount = int(input("Enter Amount: "))
                print(edit_expense(Expenses, id, amount=amount))
            elif choice == 2:
                category = input("Enter Category: ")
                print(edit_expense(Expenses, id, category=category))
            elif choice == 3:
                date = input("Enter Date: ")
                print(edit_expense(Expenses, id, date=date))
            elif choice == 4:
                description = input("Enter Description: ")
                print(edit_expense(Expenses, id, description=description))
            else:
                print("Invalid Choice")
            writer(
                Expenses,
            )
        elif choice == 4:
            id = int(input("Expense Id: "))
            print(delete_expense(Expenses, id))
            writer(
                Expenses,
            )
        elif choice == -1:
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
