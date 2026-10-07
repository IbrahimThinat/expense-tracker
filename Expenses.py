"""
Expense-handling functions.
"""


def add_expense(expenses, desc, amount):
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return
    expenses.append({"desc": desc, "amount": amount})
    print(f"Added: {desc} - {amount:.2f}")


def list_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['desc']} - {e['amount']:.2f}")


def total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total: {total:.2f}")