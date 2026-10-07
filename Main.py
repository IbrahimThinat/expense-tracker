"""
Tiny CLI Expense Tracker.
Run it with: python main.py
"""

from expenses import add_expense, list_expenses, total_expenses


def print_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Show total")
    print("4. Quit")


def main():
    expenses = []
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            desc = input("Description: ")
            amount = input("Amount: ")
            add_expense(expenses, desc, amount)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()