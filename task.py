tasks=[]
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added Successfully")
    elif choice==2:
        print("### Your Tasks ###")
        for task in tasks:
            print(task)
    elif choice==3:
        index=int(input("Enter the index of task you want to delete..."))
        if index>=len(tasks):
            print("We Dont have that Task to Delete..")
        else:
            tasks.pop(index)
            print("Task Deleted Successfully")
    elif choice==4:
        break
    else:
        print("You have Choosen Inavlid Option..Please check it once...")
    
