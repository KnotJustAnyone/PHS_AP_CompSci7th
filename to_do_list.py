class to_do_list:
    def _init_(self):
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        return None

    def remove_tasks(self,task_name): #lets user remove tasks from list
        return None

    def check_tasks(self,task_name): #checks off completed tasks
        #returns True or False boolean
        return None

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat
                                
        def interval(self):
        #choose the interval of repetition 
           return None

#Test for add_task
from todo import add_task

def test_add_task():
tasks = []
updated_tasks = add_task(tasks, "Finish homework", "high")
assert len(updated_tasks) == 1
task = updated_tasks[0]
assert task["name"] == "Finish homework"
assert task["priority"] == "high"
assert task["completed"] is False

def test_add_task_default_priority():
tasks = []
add_task(tasks, "Clean room")
assert tasks[0]["priority"] == "medium"
assert tasks[0]["completed"] is False
