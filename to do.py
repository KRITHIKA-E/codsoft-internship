tasks = []

def display_tasks():
    print("\n Your To-Do List ")
    if not tasks:
        print("No tasks yet.")
    else:
        index=1
        while index<=len(tasks):
            print(f"{index}. {tasks[index-1]}")
            index+=1
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def delete_task(del_task):
    if del_task in tasks:
        tasks.remove(del_task)
        print(f"Task '{del_task}' deleted successfully!")
    else:
        print(f"Task '{del_task}' is not in the list!" )
def main():
    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")
        
        switch_case = {
            '1': display_tasks,
            '2': lambda: add_task(input("Enter the task: ")),
            '3': lambda: delete_task(input("Enter the task to delete: ")),
            '4': lambda: print("Exiting the To-Do List application. Goodbye!")
        }.get(choice, lambda: print("Invalid choice. Please enter a number between 1 and 4."))
        
        if callable(switch_case):
            switch_case()
        else:
            break

if __name__ == "__main__":
    main()
