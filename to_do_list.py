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
            
    def print_toDoList(self):
        printYN = input("Do you want to print your to do list?")
        if printYN == "yes":
            for task in self.list:
                print(task)
        else:
            print("Not printing list")
