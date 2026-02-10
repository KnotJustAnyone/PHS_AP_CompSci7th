import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = json.load(f)

            # Convert old string tasks to new format
            new_tasks = []
            for task in tasks:
                if isinstance(task, str):
                    new_tasks.append({
                        "title": task,
                        "completed": False
                    })
                else:
                    new_tasks.append(task)

            return new_tasks
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def show_task_counts(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    remaining = total - completed

    print("\nTask Summary:")
    print(f"Total: {total} | Completed: {completed} | Remaining: {remaining}")
    
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour current tasks:")
    for i, task in enumerate(tasks, 1):
        if task["completed"]:
            print(f"{i}. [✓ COMPLETED] {task['title']}")
        else:
            print(f"{i}. [ ] {task['title']}")

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
                tasks.append({
                    "title": title,
                    "completed": False
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

