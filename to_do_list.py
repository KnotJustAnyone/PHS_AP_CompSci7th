class to_do_list:
    def _init_(self):
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
