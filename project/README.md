
# Expense Management System
### Video Demo: https://www.youtube.com/watch?v=8rmDh11u5_U
This is a simple Expense Management System implemented in Python. It allows users to add, edit, delete, and generate reports of their expenses. The expenses are stored in a CSV file, and each expense entry includes the amount, category, date, and description.

## Features

- **Add Expense**: Allows you to add a new expense with a unique ID, amount, category, date, and description.
- **Edit Expense**: Edit the details of an existing expense using its unique ID.
- **Delete Expense**: Remove an expense from the list using its unique ID.
- **Generate Report**: Display a report of all the stored expenses.
- **Persistent Storage**: Expenses are saved to a CSV file and reloaded when the program is restarted.

## Project Structure

```
project/
│
├── project.py
├── test_project.py
└── README.md
```


- `project.py`: The main Python script containing the implementation of the expense management system.
- `test_project.py`: The unit tests of the project.
- `README.md`: This README file.

## Classes

### `Category`
Represents the category of an expense.
- **Attributes:**
  - `_category` (str): The category of the expense.

- **Methods:**
  - `category`: Getter and setter for the category.
  - `__str__()`: Returns the string representation of the category.

### `Expense`
Represents an expense.
- **Attributes:**
  - `_amount` (int): The amount of the expense.
  - `_category` (Category): The category of the expense.
  - `_date` (str): The date of the expense.
  - `_description` (str): A description of the expense.

- **Methods:**
  - `amount`: Getter and setter for the amount.
  - `category`: Getter and setter for the category.
  - `date`: Getter and setter for the date.
  - `description`: Getter and setter for the description.
  - `__str__()`: Returns the string representation of the expense.

## Functions

### `add_expense(Expenses, id, amount, category, date, description)`
Adds a new expense to the `Expenses` dictionary.

### `edit_expense(Expenses, id, amount=0, category="", date="", description="")`
Edits an existing expense in the `Expenses` dictionary.

### `delete_expense(Expenses, id)`
Deletes an expense from the `Expenses` dictionary.

### `generate_report(Expenses)`
Generates a report of all stored expenses.

### `writer(Expenses)`
Writes the `Expenses` dictionary to a CSV file.

### `reader(Expenses)`
Reads expenses from the CSV file into the `Expenses` dictionary.

### `menu()`
Displays the main menu and handles user input.

### `main()`
Main function that drives the application.

## Usage

1. Run the `project.py` script.

```bash
python project.py
```

2. Follow the on-screen prompts to add, edit, delete, or view expenses.

## Requirements

- Python 3.x
- The `csv` library is used (It is built-in with Python).

## Notes

- Ensure that `Expense.csv` is in the same directory as the script, or it will be created when you run the program.
- The program is designed to handle basic expense tracking with a simple command-line interface.

