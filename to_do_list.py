class to_do_list:
    def _init_(self):
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        return None

    def remove_tasks(self,task_name): #lets user remove tasks from list
        return None

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

    def check_tasks(self,task_name): #checks off completed tasks
        #returns True or False boolean
        return None

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat
                                
        def interval(self):
        #choose the interval of repetition 
           return None
