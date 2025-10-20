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

    def repeated_tasks_test(task_name):
        print(f"Repeating task: {task_name}")
        for i in range(3):
            print(f"Task '{task_name}' repetition {i + 1}")
    
     repeated_tasks_test("Clean Room")
                                
        def interval(self):
        #choose the interval of repetition 
           return None
