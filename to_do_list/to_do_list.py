def add_task():
  task = input("Enter task: ")
  with open("tasks.txt", 'a') as file:
    file.write(f"[ ] {task}\n")
  print("\nTask Added")

def show_tasks():
  try:
    with open("tasks.txt", 'r') as file:
      tasks = file.readlines()
    if tasks:
      print("\nYour tasks: ")
      for i, task in enumerate(tasks, start = 1):
        print(f"{i}. {task.strip()}")
  except FileNotFoundError:
    print('No tasks found, please add task first. ')
    
def mark_as_completed():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks to mark as completed.")
            return
        
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[X]")
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks file found. Add a task first.")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks to delete.")
            return
        
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks file found. Add a task first.")

def main():
  while True:
    print("\nWelcome in to do list !")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Mark a task as completed")
    print("4. Delete task")
    print("5. Exit")
    try:
      choice = input("\nPlease choose an option: ")
      print("\n")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 5.")
      continue 
    
    match choice:
      case "1":
        add_task()
      case "2": 
        show_tasks()
      case "3": 
        mark_as_completed()
      case "4":
        delete_task()
      case "5":
        print("Exiting ToDoList. Bye !")
        break
      case _:
        print("Invalid option, try again !")
      


if __name__ == "__main__":
  main()
