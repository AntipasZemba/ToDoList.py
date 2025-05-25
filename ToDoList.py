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

# Function to display all tasks with their completion status
def view_tasks():
    if not tasks:
        print("No tasks in your list.") # Inform user if list is empty
    else:
        print("\nYour tasks:")
        for index, t in enumerate(tasks, start=1):
            # show ✅ for completed tasks, ❌ for incomplete
            status = "✅" if t["done"] else "❌"
            print(f"{index}. {t['task']} [{status}]")

# Function to mark a specific as completed
def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True # Set the "done" status to True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.") # Handle non-integer input

# Function to delete a task from list
def delete_task():
    view_tasks() # Show current tasks
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1) # Remove the selected task
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.") # Handle non-integer input


# 🔁 Main loop: continually show the menu and respond to user choices
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
