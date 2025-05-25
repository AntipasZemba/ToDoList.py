# List to store tasks; each task is a dictionary with a description and completion status.
tasks = []

# Function to display the menu options to the user.
def show_menu():
    print("\n=== TO DO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task":task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks in your list.")
    else:
        print("\nYour tasks:")
        for index, t in enumerate(tasks, start=1):
            status = "✅" if t["done"] else "❌"
            print(f"{index}. {t['task']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# 🔁 Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
