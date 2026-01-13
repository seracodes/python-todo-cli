def show_menu():
    print("\n--- TO DO MENU ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
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
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ")
            if task.strip():
                tasks.append(task)
                save_tasks(tasks)
                print("Task added!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        tasks.pop(num - 1)
                        save_tasks(tasks)
                        print("Task deleted!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
