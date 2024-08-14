class Checklist():

    def __init__(self):

        self._tasklist = []



    def add(self, task):

        if task == "":
            raise Exception("No tasks added, please enter a task")
        
        self._tasklist.append(task)



    def tasklist(self):
    
        return self._tasklist
    

    
    def incomplete_tasks(self, index):
        

        self._tasklist.pop(index)

        return self._tasklist 