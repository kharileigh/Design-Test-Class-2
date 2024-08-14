import pytest
from lib.checklist import *


"""
# Checklist instantiated correctly
# """
# def test_checklist_instantiated():
    
#     checklist = Checklist()
#     assert checklist == []


"""
Given no input -- empty string
#raises exception
"""
def test_add_no_input():

    checklist = Checklist()
    with pytest.raises(Exception) as err:
        checklist.add("") 

    assert str(err.value) == "No tasks added, please enter a task"




###  -------- ADD
"""
Given correct input - one task added
#returns desired result - shows lists including new task
"""
def test_add_task_view_tasks():
    
    checklist = Checklist()
    checklist.add("Unit 2 Assignment")
    checklist.add("Unit 3 Assignment")

    assert checklist.tasklist() == ["Unit 2 Assignment", "Unit 3 Assignment"]





###  -------- REMOVE TASK
"""
Given tasklist -- 
remove completed task --- using position in list
#returns desired result -- tasklist removing current task
"""
def test_incomplete_tasks():
    checklist = Checklist()
    checklist.add("Complete Unit 2 Assignment")
    checklist.add("Complete Unit 3 Assignment")
    checklist.add("Complete Unit 4 Assignment")

    # get tasklist
    # remove first task -- using index
    # return list
    assert checklist.incomplete_tasks(0) == ["Complete Unit 3 Assignment", "Complete Unit 4 Assignment"]