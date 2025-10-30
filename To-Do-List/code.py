
from datetime import datetime
import os

print("===== TO DO LIST =====")
tasks=[]

#menu
def menu():
    print("\nEnter 1 to add task.")
    print("Enter 2 to remove task.")
    print("Enter 3 to display tasks list.")
    print("Enter 4 to save the Tasks Record.")
    print("Enter 5 to load Previous Records.")
    print("Enter 6 to Clear Saved Records!")
    print("Enter 7 to exit the program.")

    choice=input("\nEnter your choice:")
    return choice

#Function to add task
def add_task():
    task=input("Add the task:")
    now=datetime.now().strftime("Date - %Y:%m:%d  Time: %H-%M-%S")
    task_with_time= f"{task.title()} , (added on {now}) "
    tasks.append(task_with_time)
    print("\nTask added Successfully!\n")

#Function to remove task
def remove_task():
    if tasks:
     try:
       to_rem = int(input("Enter task number to remove: "))
       tasks.pop(to_rem - 1) 
       print("\nTask removed Successfully!\n")
     except(ValueError,IndexError):
       print("Invalid task number , Try Again...")
    else:
      print("No tasks to remove!")

#Function to display task
def display_tasks():
    if tasks:
     print("\nThe Tasks are:")
     for index,task in enumerate(tasks,start=1):
      print(f"Task {index} - {task}")

    else:
      print("No Tasks were added to display\n")

#Function to save records
def save_records():

  if tasks:
     # Get the directory where this script is located
    folder_path = os.path.dirname(os.path.abspath(__file__))

     # Create the file path inside the same folder
    file_path = os.path.join(folder_path, "records.txt")

    with open(file_path,"a") as file:
      for index,task in enumerate(tasks,start=1):
       file.write(f"Task {index} - {task}\n")
  else:
    print("No data to save!")
    return
  print("\nTasks Saved Successfully!")
  print("Saving file to:", file_path)



#Function to load task
def load_records():
   try:
      # Get the directory where this script is located
     folder_path = os.path.dirname(os.path.abspath(__file__))

     # Create the file path inside the same folder
     file_path = os.path.join(folder_path, "records.txt")

     with open(file_path,"r") as file:
      data=file.read()
     if data:
      print(f"\nThe previous record of tasks is:\n{data}")
     else:
      print("No Records found!")
   except FileNotFoundError:
    print("The file doesn't exist!")
    
#Function to clear records
def clear_prevrec():
  confirm=input("\nAre you sure you want to Clear Saved Records (Yes or No)?")
  if confirm.lower()=="yes":

     # Get the directory where this script is located
    folder_path = os.path.dirname(os.path.abspath(__file__))

     # Create the file path inside the same folder
    file_path = os.path.join(folder_path, "records.txt")

    with open(file_path,"w") as file:
     file.write("")
    print("\nAll Saved Records are Cleared Successfully!")
  else:
    print("Clear Cancelled!...")
  
while True:
 ch=menu()

 if ch=="1":
    add_task()

 elif ch=="2":
    remove_task()

 elif ch=="3":
    display_tasks()

 elif ch=="4":
   save_records()

 elif ch=="5":
   load_records()

 elif ch=="6":
   clear_prevrec()

 elif ch=="7":
  print("Exiting program.....")
  break
 
 else:
  print("Invalid choice.")