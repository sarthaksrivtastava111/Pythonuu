# Simple Bank Account (Python)

A beginner-friendly command-line bank account program written in Python. It lets a user check their balance, deposit money, and withdraw funds using basic loops and conditional statements.

## Features
- **Check Balance:** Displays the account holder's name and current balance.
- **Deposit Money:** Adds positive amounts to the balance.
- **Withdraw Money:** Subtracts funds while preventing overdrafts and negative entries.
- **Interactive Menu:** Runs continuously until the user selects Exit.

## Requirements
- Python 3.x installed on your system (no external libraries required).

## How to Run
1. Save `bank_account.py` and `README.md` in the same folder.
2. Open your terminal or command prompt and navigate to that folder.
3. Run the script:
   ```bash
   python bank_account.py
   ```
   *(On macOS/Linux, you may need to use `python3 bank_account.py`.)*

## Example Usage
```text
Enter your name: Alex

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Choose (1-4): 2
Amount to deposit: 100
Deposited $100.00. New balance: $100.00
```