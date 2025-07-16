# cliTodoApp

Command Line Interface To Do App: 

Purpose: Let users add, view, and remove to-do items. 

Key features of program: 
    - add a new task
    - view all tasks 
    - mark task as complete 
    - remove task 
    - exit the App

Components: 
    - Add Task: User input is needed to then store that task somewhere (data structure).
    - View Tasks: Loop through stored tasks and display them. 
    - Select tasks and then remove them from storage. 
    - Mark Complete: Select a task and update its status. 
    - Exit: End the program. 


Data: 
    What data needs to be stored? 
        - Each task might need:
            - Task description (text)
            - Status (Complete/incomplete)
    Where will you store the tasks? 
        - list? vector? array? (Choosed based on the Language) - Python lists. 

Software Design: 

Use a while loop to constantly listen for user input on the command line interface when program is initiated (exe). 

Persistent storage, keeping all appended list items on a JSON file. (This has not been implemented yet but is in progress)

| Component                               | Role                                                              |
| --------------------------------------- | ----------------------------------------------------------------- |
| **Data structure (vector/list)**        | Holds the actual state of your items (persistent)                 |
| **Functions (add, delete, view, etc.)** | Perform specific actions on the data                              |
| **Loop**                                | Controls program flow and calls the right function based on input |
