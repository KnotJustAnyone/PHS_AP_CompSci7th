import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()

    if tasks:
        print("Your current tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

    print("\nEnter new tasks (press Enter on an empty line to stop):")

    while True:
        task = input("> ").strip()
        if task == "":
            break
        tasks.append(task)

    save_tasks(tasks)
    print("\nTasks saved. Come back soon! You have to finish your work!")

if __name__ == "__main__":
    main()

