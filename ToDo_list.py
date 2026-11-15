
import json
import os

File_Name = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

tasks = load_tasks()

# Save tasks to file
def save_tasks():
    with open(File_Name, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

# View all tasks
def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\n---- YOUR TASKS ----")

    for i, item in enumerate(tasks, start=1):
        status = "Completed" if item["completed"] else "Pending"
        print(f"{i}. {item['task']} - {status}")

# Update a task
def update_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter task number to update: "))

            if 1 <= number <= len(tasks):
                new_task = input("Enter updated task: ").strip()

                if new_task:
                    tasks[number - 1]["task"] = new_task
                    save_tasks()
                    print("Task updated successfully!")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

# Mark task as completed
def complete_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                save_tasks()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

# Delete a task
def delete_task():
    view_tasks()

    if tasks:
        try:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks()
                print(f"{removed['task']} deleted successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

# Main menu
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Thank you for using To-Do List!")
        break
    else:
        print("Invalid choice! Please try again.")
