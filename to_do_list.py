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

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat
                                
        def interval(self):
        #choose the interval of repetition 
           return None
