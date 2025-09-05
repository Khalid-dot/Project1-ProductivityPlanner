from datetime import datetime #to fetch date
class Task:
    def __init__(self, title, description, due_date, priority_level, status="Pending"): #constructor
        self.title=title
        self.description=description
        self.due_date=due_date
        self.priority_level=priority_level
        self.status=status
        self.creation_time=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    
    def __str__(self):
        return (f"[{self.status}] Title: {self.title}\nCreated: {self.creation_time}\nDescription: {self.description}\n"
                f"Due: {self.due_date}\nPriority: {self.priority_level}") #for formatting
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title=input("Enter Title: ")
        description=input("Description: ")
        due_date=input("Due Date: ")
        priority_level=input("Priority Level (Low/Medium/High): ")
        task=Task(title, description, due_date, priority_level)
        self.tasks.append(task)
        print("Task Added Successfully!")

    def view_tasks(self):
        if not self.tasks: #not self.tasks will be true if list(tasks) is empty
            print("No Tasks Found!")
        else:
            for idx,task in enumerate(self.tasks,1): #enumerate is a built in function to iterate over a structure and return item with the index
                print(f"{idx}. {task}\n")


    def delete_task(self, title):
        for task in self.tasks:
            if task.title.replace(" ", "").lower()==title.replace(" ", "").lower(): #convert letters into lowercase and remove spaces
                self.tasks.remove(task)
                print("Task removed successfully!")
                return
        print("Task not found!")

    def update_task(self,title):
        for task in self.tasks:
            if task.title.replace(" ", "").lower()==title.replace(" ", "").lower():
                print("Enter the new title or leave the space to keep the existing one!")
                new_title=input(f"New Title ({task.title}): ") or task.title
                new_description=input(f"New Description ({task.description}): ") or task.description
                new_DueDate=input(f"New Due Date ({task.due_date}): ") or task.due_date
                new_priority=input(f"New Due Date ({task.priority_level}): ") or task.priority_level

                task.title=new_title #overwrite the updated values
                task.description=new_description
                task.due_date=new_DueDate
                task.priority_level=new_priority

                print("Task updated successfully!")
                return
        
        print("Task not found!")
    
    def mark_complete(self,title):
        for task in self.tasks:
            if task.title.replace(" ", "").lower()==title.replace(" ", "").lower():
                task.status="Completed"
                print("Task Marked as Completed!")
                return
        print("Task not found!")

def main():
    obj=TaskManager()

    while True:
        print("------------------------- PERSONAL PRODUCTIVITY PLANNER -------------------------")
        print("1. Add Task")
        print("2. View all Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark task as Completed")
        print("6. Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            obj.add_task()

        if choice=="2":
            obj.view_tasks()
        
        if choice=="3":
            title=input("Enter the title of the task to update: ")
            obj.update_task(title)
        
        if choice=="4":
            title=input("Enter the title of the task to delete: ")
            obj.delete_task(title)
        
        if choice=="5":
            title=input("Enter the title of the task to Mark Completd: ")
            obj.mark_complete(title)
        
        if choice=="6":
            print("Thank you for using Personal Productivity Planner! ")
            break

if __name__=="__main__":
    main()








                



    

