class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
        print()

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to remove: "))
            if task_number >= 1 and task_number <= len(todo_list.tasks):
                todo_list.remove_task(todo_list.tasks[task_number-1])
            else:
                print("Invalid task number.")
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
