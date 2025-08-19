
def to_do_list():
    print("\n--- To-Do List Menu ---")
    print("1. Add a new task\n2. Show all tasks\n3. Mark tasks done\n4. Delete tasks\n5. Exit")
    choice = int(input("Enter a number (1-5): "))

def main():
    tasks = []
    while True:
        to_do_list()
        choice = int(input("Enter your choice: "))
        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_tasks(tasks):
    new_task = str(input("Add a new task: "))
    tasks.append(({"Task": new_task, "Completed": False}))
    print("Task added!")
    return

def view_tasks(tasks):
    if tasks == []:
        print("No tasks in the list.")
        return
    no = 0
    print("\n--- Your Tasks ---")
    for i, item in enumerate(tasks):
        status = "Done" if item["completed"] else "Pending"
        print(f"{i + 1}. {item['task']} [{status}]")
    
def mark_task_done(tasks):
    view_tasks(tasks)
    to_complete = int(input("Enter the number of the task you completed (number): ")) - 1
    if 0 <= to_complete < len(tasks):
        tasks[to_complete]["completed"] = True
    print("Task marked as done.")
 
def delete_task(tasks):
    to_delete = int(input("Enter the number of the task you want to delete (number): ")) - 1
    if 0 <= to_delete < len(tasks):
        tasks.pop(to_delete)
        print("Task deleted!")
        return
    else:
        print("Invalid task number.")


main()
