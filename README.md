# Python Password Strength Checker 🔒

A simple Python tool that evaluates the strength of passwords and provides **actionable feedback** to help users create stronger, more secure passwords.

---

## 🚀 Features

This script:

- Checks for **minimum length** (8 or more characters)  
- Detects **uppercase and lowercase letters**  
- Detects **numbers**  
- Detects **special characters** (`!@#$%^&*(),.?":{}|<>`)
- Flags **common weak passwords**
- Gives a **strength rating**: **Weak**, **Moderate**, or **Strong**
- Provides **friendly suggestions** to improve weak passwords

---

## 🧠 How It Works

The script scores your password based on:

1. Length (at least 8 characters)  
2. Includes at least one uppercase letter  
3. Includes at least one lowercase letter  
4. Includes at least one number  
5. Includes at least one special character  

If a password is on a *basic common list* (like `"password"`, `"123456"`), it is **penalized** to avoid weak choices.

| Score | Strength   |
|-------|------------|
| 0–2   | Weak       |
| 3–4   | Moderate   |
| 5     | Strong     |

---

## 🛠️ Installation

First, make sure you have Python 3 installed:

```bash
python --version
```
Then clone the repo (or download ZIP):
```
git clone https://github.com/DH4N453K4R4N/Password-Strength-Checker.git
cd Password-Strength-Checker
```
No external libraries or modules are required — the script uses Python’s built‑in re module.
---
▶️ Usage

Run the script using Python:
```
python Password_Strength_Checker.py
```
You’ll be prompted to enter a password:
```
Enter your password:
```
The tool will then show:

A strength rating

Suggestions to improve your password
---
📌 Example
```
Enter your password: mypassword123
Password Strength: Moderate
Suggestions to improve:
 - Add at least one uppercase letter.
 - Add at least one special character (!@#$ etc).
```
