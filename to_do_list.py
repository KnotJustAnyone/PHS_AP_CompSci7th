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

    def search_task(self, keyword):
    results = [t for t in self.tasks if keyword.lower() in t["name"].lower()]
    if not results:
        print(f"No tasks found containing '{keyword}'.")
    else:
        print(f"Tasks matching '{keyword}':")
        for task in results:
            status = "✅" if task["completed"] else "❌"
            print(f"{status} {task['name']}")
