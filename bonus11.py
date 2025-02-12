import json
from datetime import datetime

# File name where tasks are stored
TODO_FILE = 'data.json'

# Load tasks from the file
def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            data = json.load(file)
            return data['ToDolist']  # Return the list of tasks
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    data = {"ToDolist": tasks}  # Wrap tasks in the required structure
    with open(TODO_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new task
def add_task(title, time, date, full_time=False):
    tasks = load_tasks()
    new_task = {
        "title": title,
        "time": time,
        "date": date,
        "full-time": full_time
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")

# Display all tasks
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "FULL-TIME" if task['full-time'] else "PART-TIME"
            print(f"{i}- {task['title']} - {task['date']} {task['time']} - {status}")

# Mark a task as full-time
def mark_task_full_time(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['full-time'] = True
        save_tasks(tasks)
        print(f"Task {task_index} marked as FULL-TIME.")
    else:
        print("Invalid task number.")

# Search for tasks by title
def search_task(title):
    tasks = load_tasks()
    found_tasks = [task for task in tasks if title.lower() in task['title'].lower()]
    if found_tasks:
        print("Found the following tasks:")
        for i, task in enumerate(found_tasks, start=1):
            status = "FULL-TIME" if task['full-time'] else "PART-TIME"
            print(f"{i}- {task['title']} - {task['date']} {task['time']} - {status}")
    else:
        print("No tasks found matching the search.")

# Example usage
if __name__ == "__main__":
    # Add some tasks
    add_task("Go to gym", "8:00", "2025-2-12")
    add_task("Visit grandma", "10:00", "2025-2-15")

    # Display all tasks
    print("\nAll Tasks:")
    show_tasks()

    # Mark the first task as full-time
    mark_task_full_time(1)

    # Display all tasks after marking
    print("\nAll Tasks After Marking:")
    show_tasks()

    # Search for a task by title
    print("\nSearch Results for 'gym':")
    search_task("gym")