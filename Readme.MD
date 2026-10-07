# Expense Tracker

A simple command-line app for tracking everyday expenses. Add expenses, list them, and see your running total — all from the terminal.

## Features
- Add an expense with a description and amount
- List all recorded expenses
- View the total amount spent

## Requirements
- Python 3.7+

## Getting Started

Clone the repo:
```bash
git clone https://github.com/yourname/expense-tracker.git
cd expense-tracker
```

Run the app:
```bash
python main.py
```

## Usage

When you run the app, you'll see a menu:
```
=== Expense Tracker ===
1. Add expense
2. List expenses
3. Show total
4. Quit
```

Pick an option number and follow the prompts. Example:
```
Choose an option: 1
Description: Coffee
Amount: 4.50
Added: Coffee - 4.50
```

## Project Structure
```
expense-tracker/
├── main.py        # CLI menu and program loop
├── expenses.py     # Core logic: add, list, and total expenses
├── .gitignore
└── README.md
```

## Roadmap
- [ ] Save expenses to a file so they persist between runs
- [ ] Filter expenses by date or category
- [ ] Export to CSV

## License
MIT