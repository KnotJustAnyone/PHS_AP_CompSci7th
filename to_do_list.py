import random

class task:
    def __init__(self,task_name,task_done=False,interval=0):
        self.task_name = task_name
        self.task_done = task_done
        self.repetition_interval = interval

    def change_name(self,name):
        self.task_name = name

    def toggle_done(self,true_false): # To toggle task_done: toggle_done(x), where x is true or false (depending on what you want)
        self.task_done = true_false

    def set_interval(self,interval):
        self.repetition_interval = interval

    
class to_do_list:
    def __init__(self):
        self.list = [] # List of tasks. task is task = (string, boolean, int)

        # Maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        task1 = task(task_name, False, 0)
        self.list.append(task1)
        print(f"Task '{task_name}' added.")

    def list_tasks(self):
        if not self.list:
            print("You have no tasks!")
        else:
            print("Your tasks:")
            for task in self.list:
                name = task[0]
                completed = task[1]
                status = "Done" if completed else "Not done"
                print(f"- {name} [{status}]")

    def remove_tasks(self,task_name): #lets user remove tasks from list
        task_name = input ("Type in the task you want to remove: ")

    def sort_alphabetically(self): 
        self.list.sort(key=lambda t: t[0])
        print("Tasks sorted alphabetically.")

    def check_tasks(self,task_name): #Checks off completed tasks
        #returns True or False boolean
        return None
    
    def count_incomplete(self):
        return sum(1 for t in self.list if not t[1])

    def repeated_tasks(self,task_name): # Allows user to choose tasks to repeat
         """
    Allows user to choose a task and assign a repetition interval.
    repetition_interval meanings:
        0 = not repeated
        1 = daily
        7 = weekly
        30 = monthly
    """
      for i, task in enumerate(self.list):
          name, completed, interval = task
          if name == task_name:
              # Ask user to pick repetition interval
              new_interval = self.interval()
              # Replace task with updated repetition interval
              self.list[i] = (name, completed, new_interval)
              print(f"Task '{task_name}' is now set to repeat every {new_interval} day(s).")
              return

      print(f"Task '{task_name}' not found.")
                                


        def interval(self):
        # Choose the interval of repetition 
           return None

def load_todo_list(filename="todos.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No existing to-do file found")
        return []
    except Exception as e:
        print("Error loading to-do list")
        return []
import json

def save_todo_list(todo_list, filename="todos.json"):
    try:
        with open(filename, "w") as file:
            json.dump(todo_list, file, indent=4)
        print("to do list saved")
    except Exception as e:
        print("error saving to do list")
def addandlisttest():
    dog = to_do_list()
    dog.add_tasks("Do dishes")
    dog.list_tasks()
            
    def print_toDoList(self):
        printYN = input("Do you want to print your to do list?")
        if printYN == "yes":
            for task in self.list:
                print(task)
        else:
            print("Not printing list")
            
    def clear_all(self):
        self.list.clear()
        print("All tasks cleared.")

# Repeated_tasks_test("Clean Room")
                                
    def random_task(self):
        incomplete_tasks = [task for task in self.list if not task[1]]
        if not incomplete_tasks:
            print("No incomplete tasks!")
            return
        print("Try doing:", random.choice(incomplete_tasks)[0])

    def stats(self):
        done = 0
        for t in self.list:
            if t[1]:
                done += 1
        total = len(self.list)
        print(f"Completed: {done}/{total}")

    def count_tasks_by_priority(self):
        counts = {}
        for t in self.list:
            p = t.priority
            counts[p] = counts.get(p, 0) + 1
        return counts


def removeTask_test():
    taskList = ["Do math homework", "wash dishes", "walk the dog"] #the to do list
    To_be_removed = "wash dishes"
    final_list = ["Do math homework", "walk the dog"]

    action = "remove"
    remove_which_task  = 2 # Remove wash dishes
    a = int(remove_which_task) - 1 # Making it work with the index number
    removing = taskList.pop(a)

    if removing == To_be_removed and taskList == final_list:
        print("test works")
    else:
        print ("test failed")
   
    def clear_completed_tasks(self):
        new_list = []
        for task in self.list:
            if not task[1]:
                new_list.append(task)
        self.list = new_list
        print("All completed tasks have been removed from your to-do list.")

def repeated_tasks_test(task_name):
    print(f"Repeating task: {task_name}")
    for i in range(3):
        print(f"Task '{task_name}' repetition {i + 1}")
        
def check_task_test():
    todo = ToDoList()

    #some tasks
    todo.add_task("do homework")
    todo.add_task("clean room")
    todo.add_task("seal the honmoon")

    #Check an existing task
    result1 = todo.check_task("Do laundry")
    if result1 is True and todo.list[1][1] is True:
        print("checked off existing task")
    else:
        print("failed")

    #check a non-existent task
    result2 = todo.check_task("workout")
    if result2 is False:
        print("Handled missing task correctly")
    else:
        print("failed")

    #check if other tasks remain unchanged
    if todo.list[0][1] is False and todo.list[2][1] is False:
        print("other tasks unchanged")
    else:
        print("failed")

    print("Final task list state:")
    for task in todo.list:
        print(task)
    for task in self.list:
        if task[0] == task_name:
            self.list.remove(task)
            print("The task has been removed")
            break
    else:
        print("A task has not been removed.")
