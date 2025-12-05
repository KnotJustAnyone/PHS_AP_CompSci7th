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
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        task1 = task(task_name, False, 0)
        self.list.append(task1)
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
