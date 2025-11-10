class to_do_list:
    def _init_(self):
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        return None

    def remove_tasks(self,task_name): #lets user remove tasks from list
        action = input("do you want to add / remove/ or save?")

        if action == "remove":
            remove_which_task  = input ("Which task do you want to remove? type the full name of it")

            for task in self.list:
                if task[0] == remove_which_task:
                    self.list.remove(task)
                    print("The task has been removed")
                    break
                
            else:
                print("a task has not been removed")
        

    def check_tasks(self,task_name): #checks off completed tasks
        #returns True or False boolean
        return None

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat
                                
        def interval(self):
        #choose the interval of repetition 
           return None
