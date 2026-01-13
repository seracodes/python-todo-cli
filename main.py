def show_menu():
  print("\n--- TO DO LIST ---")
  print("1. View tasks")
  print("2. Add task")
  print("3. Delete task")
  print("4. Exit")

def load_tasks():
  try:
      with open("tasks.txt", "r") as file:
      return
file.read().splitlines() 
  except:
      return []

def save_tasks(tasks):
  with open("tasks.txt", "w") as file:
    for task in tasks:
      file.write(task + "\n")

def main():
  tasks = load_tasks()
  
    while True:
      show_menu()
      choice = input("Choose an option: ")
      
        if choice == "1":
          print("\nYour tasks:")
          for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
        elif choice == "2":
          task = input("Enter new task: ")
          tasks.append(task)
          save_tasks(tasks)
          print("Task added!")
          
        elif choice == "3":
          for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
          num = int(input("Enter task number to delete: "))
          tasks.pop(num - 1)
          save_tasks(tasks)
          print("Task deleted!")
          
        elif choice == "4":
          print("Goodbye!")
          break  
        else:
          print("Invalid choice!")
