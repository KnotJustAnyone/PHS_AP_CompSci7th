import random
class to_do_list:
    def __init__(self):
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        task = (task_name, False, 0)
        self.list.append(task)
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
        return None

    def check_tasks(self,task_name): #checks off completed tasks
        #returns True or False boolean
        return None

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat


        def interval(self):
        #choose the interval of repetition 
           return None

#repeated_tasks_test("Clean Room")
                                
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

def removeTask_test():
    taskList = ["Do math homework", "wash dishes", "walk the dog"] #the to do list
    To_be_removed = "wash dishes"
    final_list = ["Do math homework", "walk the dog"]

    action = "remove"
    remove_which_task  = 2 #remove wash dishes
    a = int(remove_which_task) - 1 #making it work with the index number
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