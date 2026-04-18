# 🏦 Python Bank Account System

A console-based personal bank account system built with Python.  
This project covers **Object-Oriented Programming (OOP)**, **custom exceptions**, and **error handling**.

---

## ✨ Features

- 🏧 Create a bank account with an opening balance
- 💰 Deposit money
- 💸 Withdraw money (with balance check)
- 🔄 Transfer money between two accounts
- 📋 View full transaction history with timestamps
- ❌ Custom error handling for invalid inputs

---

## 🛠️ Concepts Used

| Concept | Where Used |
|---|---|
| OOP (Classes & Objects) | `BankAccount` class |
| Encapsulation | Private `__balance`, `__transactions` |
| Custom Exceptions | `InsufficientFundsError`, `InvalidAmountError` |
| Error Handling | `try/except` blocks |
| Properties | `@property` for balance |

---

## 🚀 How to Run

```bash
python bank_account.py
```

No external libraries needed — pure Python! 🐍

---

## 📁 Project Structure

```
python-bank-account-system/
│
├── bank_account.py   # Main project file
├── README.md         # Project documentation
└── .gitignore        # Python gitignore
```

---

## 📌 Example Output

```
🏦 Welcome to PyBank!

✅ ₹2000.00 deposited. New balance: ₹7000.00
✅ ₹500.00 withdrawn. New balance: ₹6500.00
🔄 ₹1500.00 transferred to Bob's account.

⚠️ Testing Error Handling:
❌ InsufficientFundsError: Cannot withdraw ₹99999.00. Available balance: ₹2500.00
❌ InvalidAmountError: Amount must be positive. Got: ₹-200
❌ TypeError: Amount must be a number, got str
```

---

## 👩‍💻 Author

**Yachika Sharma** — [@yachikasharma-art](https://github.com/yachikasharma-art)

---

⭐ If you found this helpful, consider giving it a star!
