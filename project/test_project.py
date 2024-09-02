from project import add_expense, delete_expense, edit_expense, reader


def test_add():
    Expenses = {}
    assert add_expense(Expenses, 1, 100, "Food", "2024-08-25", "Lunch") == "Done"


def test_remove():
    Expenses = {}
    add_expense(Expenses, 1, 100, "Food", "2024-08-25", "Lunch")
    assert delete_expense(Expenses, 1) == "Done"


def test_modify():
    Expenses = {}
    reader(
        Expenses,
    )
    assert edit_expense(Expenses, 1, amount=200) == "Done"
