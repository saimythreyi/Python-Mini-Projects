tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Task '{task}' added!")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"🗑️ Task '{removed}' deleted!")
    except IndexError:
        print("Invalid task number.")

print("📝 Welcome to the To-Do List CLI!")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "4":
        print("Thank you... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
