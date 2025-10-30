# 📝 To-Do List (CLI-Based Python Project)

A simple yet functional **Command Line Interface (CLI) To-Do List** application built in Python.  
This program allows users to **add, remove, display, save, load, and clear tasks** with automatic timestamping and persistent storage — a perfect beginner-friendly project to strengthen file handling and modular programming skills.

---

## ⚙️ Features

- ➕ **Add Tasks** – Add new tasks with automatic date and time stamps.  
- ❌ **Remove Tasks** – Delete any task by its number in the list.  
- 📋 **Display Tasks** – View all current tasks stored in memory.  
- 💾 **Save Records** – Save your session’s tasks to a file (`records.txt`).  
- 📂 **Load Records** – Load previously saved tasks from the same file.  
- 🧹 **Clear Records** – Wipe all saved tasks from `records.txt`.  
- 🚪 **Exit Option** – Cleanly exit the program when done.

---

## 🧠 Concepts Used

- Python **Functions** for modular and reusable code.  
- **File Handling** (`open`, `write`, `read`) for persistent storage.  
- **Datetime Module** for timestamps on every added task.  
- **Error Handling** (`try`-`except`) for robust user input management.  
- **os.path** for automatic path detection to save data inside the same folder.

---

## 🖥️ How to Run

1. Clone or download this repository.  
2. Open the project folder in **VS Code** or any IDE.  
3. Run the script in your terminal:
   ```bash
   python to_do_list.py
