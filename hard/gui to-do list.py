import tkinter as tk
from pathlib import Path

# Ensure folder exists
save_folder = Path("to-do list saves")
save_folder.mkdir(parents=True, exist_ok=True)

save_file = save_folder / "save1.txt"

# Window
to_do_list_win = tk.Tk()
to_do_list_win.title("GUI To-Do list")
to_do_list_win.geometry("700x600")

# Icon (make sure the path is correct for your machine)
my_icon = "D:\VS code Python files\data\To-do list icon.ico"
to_do_list_win.iconbitmap(my_icon)

# Instruction label
tk.Label(
    to_do_list_win,
    text="What do you want to do today? Don't worry, your work is stored in a .txt file",
    font=("Arial", 14),
    wraplength=600
).pack(pady=10)

# One Text widget for entering tasks
task_entry = tk.Text(to_do_list_win, height=2, width=40, font=("Arial", 14))
task_entry.pack(pady=10)

# Display area for tasks
tasks_display = tk.Listbox(to_do_list_win, width=50, height=15, font=("Arial", 14))
tasks_display.pack(pady=10)

def add_task():
    task = task_entry.get("1.0", "end-1c").strip()
    if task:
        # Add to display
        tasks_display.insert("end", task)
        # Append to file
        with save_file.open("a", encoding="utf-8") as f:
            f.write(task + "\n")
        task_entry.delete("1.0", "end")

def delete_task():
    try:
        # Get selected index
        index = tasks_display.curselection()[0]
        task = tasks_display.get(index)
        tasks_display.delete(index)

        # Rewrite file without the deleted task
        tasks = tasks_display.get(0, "end")
        with save_file.open("w", encoding="utf-8") as f:
            for t in tasks:
                f.write(t + "\n")
    except IndexError:
        pass  # no selection

# Buttons
tk.Button(to_do_list_win, text="Add Task", font=("Arial", 14), command=add_task()).pack(pady=5)
tk.Button(to_do_list_win, text="Delete Task", font=("Arial", 14), command=delete_task()).pack(pady=5)

# Load existing tasks at startup
if save_file.exists():
    for line in save_file.read_text(encoding="utf-8").splitlines():
        tasks_display.insert("end", line)

to_do_list_win.mainloop()
