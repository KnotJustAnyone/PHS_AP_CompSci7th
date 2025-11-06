class to_do_list:
    def _init_(self):
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        task = (task_name, False, 0)
        self.list.append(task)
        print(f"Task '{task_name}' added.")
    def remove_tasks(self,task_name): #lets user remove tasks from list
        return None

    def check_tasks(self,task_name): #checks off completed tasks
        #returns True or False boolean
        return None

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat
                                
        def interval(self):
        #choose the interval of repetition 
           return None

def show_menu():
    print("====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Set Repeat Interval")
    print("=============================")


def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Enter your choice 1-6").strip()

        if choice == "1":
            todo.show_tasks()

        elif choice == "2":
            name = input("Enter task name").strip()
            if name:
                todo.add_tasks(name)
            else:
                print("Task name cannot be empty")

        elif choice == "3":
            name = input("Enter task name to remove").strip()
            todo.remove_tasks(name)

        elif choice == "4":
            name = input("Enter task name to mark as done").strip()
            todo.check_tasks(name)

        elif choice == "5":
            name = input("Enter task name to repeat").strip()
            interval = input("Enter repeat interval (in days)").strip()
            if interval.isdigit():
                todo.repeated_task(name, int(interval))
            else:
                print("Invalid interval")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
