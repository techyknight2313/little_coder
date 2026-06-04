Tasks = []

import json

def show_stats():

    total = len(Tasks)

    completed = 0

    for task in Tasks:
        if task["done"]:
            completed += 1

    pending = total - completed

    if total > 0:
        completion_rate = (completed / total) * 100
    else:
        completion_rate = 0

    print(f"""
===== TASK STATISTICS =====
Total Tasks      : {total}
Completed Tasks  : {completed}
Pending Tasks    : {pending}
Completion Rate  : {completion_rate:.1f}%
===========================
""")

def get_status(task):

    return "Completed" if task["done"] else "Not completed"

def display_task(task):
    
    status = get_status(task)
    print(f"""
    Task Name : {task['task']}
    Priority  : {task['priority']}
    Due Date  : {task['due']}
    Status    : {status} 
    """)
        

def load_tasks():
    global Tasks

    try:
        with open("Task.json", "r") as file:
            Tasks = json.load(file)
    except FileNotFoundError :
        Tasks = []

def save_tasks():
        global Tasks
        with open("Task.json", "w") as file:
            json.dump(Tasks, file, indent=4)

def show_tasks():
    if Tasks:           
        show_stats()
        print ("Your current tasks are:" )
        for i, task in enumerate(Tasks, 1):
            print(f"Task #{i}")
            display_task(task)
            print("-"*40)
                            
    else:
        print("No tasks avaiblable")

def add_tasks() :
    from datetime import datetime
    show_tasks()
    task = input("Enter Task you want to add to the list or \n PRESS 0 to cancel the action \n") 
    pri = input ("Enter the priority of task. \n") 
    due_date = input ("Enter the due date of task. \n")
    try :
        datetime.strptime(due_date, "%Y-%m-%d")
        if task.strip()== "" :
            print ("Task cannot be empty.")
        elif task == "0" :
            print("Action cancelled")
        else :
            Tasks.append({"task" : task , "done" : False , "priority": pri , "due" : due_date })
            print(f"Added {task} to the list")
            save_tasks()
        print (f"Total number of tasks : {len(Tasks)}")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")

def remove_tasks() :
    show_tasks()
    try:
    
        task_number = int(input("Enter task number you want to remove: or \n  PRESS 0 to cancel the action \n"))
        if task_number == 0 :
            print ("Action cancelled")
        elif 1<= task_number <= len( Tasks) :
            confirmation = input(f"Are you sure you want to remove the selected task ie. {task_number} \n Choose y/n \n ")
            if confirmation.lower() == "y" :
                removed = Tasks.pop(task_number - 1 )
                print(f"{removed['task']} removed")
            elif confirmation.lower() == "n" :
                print("Action cancelled")
            save_tasks()
        else : 
            print ("Invalid task number")
    except ValueError:
        print ("Please enter a valid number")

def mark_tasks() :
    show_tasks()
    try:
        option = int (input("Enter task number you want to mark as done/undone \n"))
        if 1<= option <= len (Tasks) :
            Tasks[option -1] ["done"] = not Tasks[option -1] ["done"]
            status = get_status(Tasks[option-1])
            print(f"{Tasks[option-1]['task']} marked as {status}")
        else :
            print("Invalid response")
        save_tasks()
    except ValueError :
        print ("Please enter a Valid number ") 

def update_tasks() :
    from datetime import datetime
    try:
        option = int (input("Enter task number you want to Update \n"))
        if 1<= option <= len(Tasks):     

            old_task = Tasks[option - 1]["task"]
            old_pri = Tasks[option - 1]["priority"]
            old_due = Tasks[option - 1]["due"]             
        
            task_n = input ("Updated name for the task OR press 0 to keep it unchanged\n")
            pri_n = input ("Updated priority for the task OR press 0 to keep it unchanged\n")
            due_date_n = input ("Updated due date for the task OR press 0 to keep it unchanged\n")

            if due_date_n != "0" :
                try :
                    datetime.strptime(due_date_n, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD")
                    return
    
            confirmation = input(f"Are you sure you want to edit the selected task ie. {option} \n Choose y/n \n")
            if confirmation.lower() == "y" :   
                if task_n != "0" :
                    Tasks[option -1] ["task"] = task_n             
                if pri_n != "0":
                    Tasks[option -1] ["priority"] = pri_n
                if due_date_n != "0" :
                    Tasks[option -1] ["due"] = due_date_n
                print(f"Changed {old_task} {old_pri} {old_due} to {Tasks[option -1] ['task']} {Tasks[option -1] ['priority']} {Tasks[option -1] ['due']}")
                save_tasks()
            elif confirmation.lower() == "n" :
                print("Update cancelled")
            else :
                print("Please choose a valid number")  
                
    except ValueError:
        print ("Please choose a valid number")    

def search_tasks():
    find= input("Enter the keyword you want to find in the task list \n")
    found = False
    for i, task in enumerate(Tasks,1): 
        status = get_status(task)      
        if (
            find.lower() in task["task"].lower()
            or
            find.lower() in task["priority"].lower()
            or
            find.lower() in task["due"].lower()
            or 
            find.lower() in status.lower()
        ):
            found=True
            print(f"Task #{i}")
            display_task(task)
            print("-" * 40)
    if not found :
        print("No keyword matches")
            
                         

load_tasks()    
        

while True :

        print (" Choose an action you want to proceed with \n 1. View Tasks \n 2. Add Tasks \n 3. Remove Task \n 4. Mark Task done/undone \n 5. Update task list \n 6. Search Tasks \n 7. Exit Task list \n ")
        Choice = input("Enter your Choice (1-7) \n")

        if Choice == "1" :
            show_tasks() 
        
        elif Choice == "2" :        
            add_tasks()
            
        elif Choice == "3" :
            remove_tasks()        

        elif Choice == "4" : 
            mark_tasks() 

        elif Choice == "5" :
            update_tasks()
        
        elif Choice == "6" :
            search_tasks()
          
        elif Choice == "7" :
            print("Ending task list....")   
            break
        

