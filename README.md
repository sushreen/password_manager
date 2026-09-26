# 🔑 Personal Password Manager

A lightweight, terminal-based **Python CLI application** designed to manage and generate credentials securely on your local machine.

---

## 🚀 Features

* **💾 Save Passwords:** Store website credentials instantly into a local flat-file text database.
* **🔍 View Stored Data:** Retrieve and list all saved websites along with their matching passwords.
* **🎲 Password Generator:** Instantly create strong, random 12-character passwords using uppercase/lowercase letters, digits, and special characters.
* **🔄 Persistent Storage:** Automatically loads pre-existing credentials from `passwords.txt` every time the script starts up.

---

## 🛠️ Requirements

* **Python 3.x**
* No external third-party dependencies are required (built entirely using Python's standard `random` and `string` library modules).

---

## 💻 How to Run

1. Open your terminal window and navigate to the project folder:
   ```bash
   cd /path/to/password_manager
   ```

2. Execute the application script:
   ```bash
   python3 password_manager.py
   ```

---

## 📂 Project Structure

* `password_manager.py` — The core application containing execution logic and user menus.
* `passwords.txt` — The persistent flat-file text storage holding your saved credentials.
* `README.md` — Project documentation and setup guidelines.

