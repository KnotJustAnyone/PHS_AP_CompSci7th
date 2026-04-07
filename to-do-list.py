import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = json.load(f)
            new_tasks = []
            for task in tasks:
                if isinstance(task, str):
                    new_tasks.append({
                        "title": task,
                        "completed": False,
                        "due_date": None
                    })
                else:
                    if "due_date" not in task:
                        task["due_date"] = None
                    new_tasks.append(task)
            return new_tasks
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def validate_due_date(due_date):
    """Return the date string if valid format, otherwise keep as entered"""
    if not due_date:
        return None
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        return due_date  # **allow other strings**

def show_task_counts(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    remaining = total - completed

    print("\nTask Summary:")
    print(f"Total: {total} | Completed: {completed} | Remaining: {remaining}")

    # **Bold Addition: Enhanced Celebration**
    if total > 0 and remaining == 0:
        print("\n" + "="*40)
        print("🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉")
        print("You completed all your tasks! 🎯")
        print("="*40 + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour current tasks:")
    today = datetime.today().date()  # **Bold Addition: get today's date for overdue check**
    for i, task in enumerate(tasks, 1):
        due_display = f"(Due: {task['due_date']})" if task.get("due_date") else ""
        overdue_display = ""  # **Bold Addition: for overdue warning**
        # **Bold Addition: check overdue**
        if task.get("due_date"):
            try:
                due_date_obj = datetime.strptime(task['due_date'], "%Y-%m-%d").date()
                if not task["completed"] and due_date_obj < today:
                    overdue_display = "⚠️ OVERDUE"
            except ValueError:
                pass  # allow free text
        status = "[✓ COMPLETED]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['title']} {due_display} {overdue_display}")

def main():
    tasks = load_tasks()

    while True:
        show_task_counts(tasks)
        show_tasks(tasks)

        print("""
Options:
1. Add a new task
2. Mark task as complete
3. Clear completed tasks
4. Exit
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter task: ").strip()
            if title:
                due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
                due_date = validate_due_date(due_date)

                tasks.append({
                    "title": title,
                    "completed": False,
                    "due_date": due_date
                })
                save_tasks(tasks)

        elif choice == "2":
            num = input("Enter task number to complete: ").strip()
            if num.isdigit():
                index = int(num) - 1
                if 0 <= index < len(tasks):
                    tasks[index]["completed"] = True
                    save_tasks(tasks)

        elif choice == "3":
            tasks = [task for task in tasks if not task["completed"]]
            save_tasks(tasks)
            print("Completed tasks cleared.")

        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Come back soon!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
