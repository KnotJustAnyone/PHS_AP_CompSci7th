class to_do_list:
    def _init_(self):
        self.list = [] #list of tasks. task is task = (string, boolean, int)

        #maybe add class for tasks with self.start day or self.repetition_interval

    def add_tasks(self,task_name): #lets user add tasks to list.  
        return None

    def remove_tasks(self,task_name): #lets user remove tasks from list
        action = input("do you want to add / remove/ or save?")

        if action == "remove":
            remove_which_task  = input ("Which task do you want to remove? 1 - # (any number from 1 to the largest numbered task)")

            if remove_which_task.isdigit(): #if their response is a number
                a = int(remove_which_task) - 1 #making it work with the index number

                if 0<= a <= len(self.list):
                    removing = self.list.pop(a)
                    print ("Task #" + remove_which_task + "has been removed --" + removing)

            else:
                print("Please type in a number in the range of the tasklist numbers")
        

    def check_tasks(self,task_name): #checks off completed tasks
        #returns True or False boolean
        return None

    def repeated_tasks(self,task_name): #allows user to choose tasks to repeat
                                
        def interval(self):
        #choose the interval of repetition 
           return None
