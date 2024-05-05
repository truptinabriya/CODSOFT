# Dictionary to store tasks
tasks = {}


def add_task(task_id, title, description, due_date, priority):
    tasks[task_id] = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'status': 'Pending'
    }


def list_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for task_id, task_details in tasks.items():
            print(f"Task ID: {task_id}")
            for key, value in task_details.items():
                print(f"{key.capitalize()}: {value}")
            print()


def remove_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print("Task removed successfully!")
    else:
        print("Task not found!")


def main():
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority (low/medium/high): ")
            add_task(len(tasks) + 1, title, description, due_date, priority)
            print("Task added successfully!")

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
