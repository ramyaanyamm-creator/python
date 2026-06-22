tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")

    elif choice == "4":
        break