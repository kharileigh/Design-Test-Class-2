

## 1. Describe the Problem

*User Story*

Nouns : classes & attributes
Verbs : methods & functionality

## 2. Design the Class Interface

-  initializer
- public properties
- public methods with all parameters
- return values
- side-effects


```python


class Name:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   
        # Side effects:
        #  
        pass

    def (self):
        # Parameters:
        #   
        # Returns:
        #   
        # Side-effects
        #  
        pass 

    def remind(self):
        # Returns:
        #   
        # Side-effects:
        #   
        pass 
```

## 3. Create Examples as Tests



``` python
# EXAMPLE

"""
Given no input
#raises exception
"""
instance = Class()
instance.function_call() -- error

"""
Given correct input
#returns desired result
"""
instance = Class()
instance.function_call(arg) -- assert vaue

```


## 4. Implement the Behaviour

Write Test -- (RED) Fail Test -- Implement Behaviour -- (GREEN) Pass Test 
Write New Test -- (RED) Fail Test -- Refactor to Implement Added Behaviour -- (GREEN) Pass Test 

*repeat until program is complete*  
