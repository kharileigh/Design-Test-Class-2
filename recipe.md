

## 1. Describe the Problem

*User Story*

***As a user***
***So that I can keep track of my tasks***
***I want a program that I can add todo tasks to and see a list of them.***

***As a user***
***So that I can focus on tasks to complete***
***I want to mark tasks as complete and have them disappear from the list.***


#### Nouns : classes & attributes
tasks -- todo(state : original when added) -- to complete(state : those untouched in program)

#### Verbs : methods & functionality
add -- view -- mark complete - disappear



## 2. Design the Class Interface

-  initializer
- public properties
- public methods with all parameters
- return values
- side-effects


```python

class Checklist:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #  creates an empty list
        pass

    def add(self, task):
        # Parameters:
        #   string 
        # Returns:
        #   none
        # Side-effects
        #  adds task to a list
        pass 

    def tasklist(self):
        # Returns:
        #   list of all tasks to complete
        # Side-effects:
        #   none
        pass 
    
    def incompleted_tasks(self):
        # Parameters :
        #   list containig tasks
        # Returns:
        #   returns lists of tasks -- now only incomplete ones
        # Side-effects:
        #   removes completed tasks 
        pass 



```

## 3. Create Examples as Tests



``` python

# """
# Checklist instantiated correctly
# """
# def test_checklist_instantiated():
    
#     # checklist = Checklist()
#     # assert checklist.tasklist == []


"""
Given no input
#raises exception
"""
def test_add_no_input():
    # checklist = Checklist()
    # checklist.add() 

    # ERROR : "No tasks added, please enter a task"
    

"""
Given correct input - one task added
#returns desired result - shows lists including new task
"""
def test_add_task_view_tasks():
    # checklist = Checklist()
    # checklist.add("Complete Unit 2 Assignment")

    # assert checklist.tasklist(["Complete Unit 2 Assignment"])

"""
Given tasklist -- 
remove completed task --- using position in list
#returns desired result -- tasklist removing current task
"""
def test_incomplete_tasks():
    # checklist = Checklist()
    # checklist.add("Complete Unit 2 Assignment")
    # checklist.add("Complete Unit 3 Assignment")
    # checklist.add("Complete Unit 4 Assignment")

    # assert checklist.incomplete(["Complete Unit 3 Assignment", "Complete Unit 4 Assignment"])


```


## 4. Implement the Behaviour

Write Test -- (RED) Fail Test -- Implement Behaviour -- (GREEN) Pass Test 
Write New Test -- (RED) Fail Test -- Refactor to Implement Added Behaviour -- (GREEN) Pass Test 

*repeat until program is complete*  
