i = 1

tasks = []
while i != 0:
    print("\nInsert the number corresponding to the action you want to perform."
          "\n1.Insert a new task."
          "\n2. Remove a task."
          "\n3. Show all existing tasks."
          "\n4. Close the program.")
    choice = input()
    choice = int(choice)

    if choice == 1:
        print("Insert new task")
        newtask = input()
        tasks.append(newtask)
    elif choice == 2:
        print("Which task would you like to remove?")
        removetask = input()
        tasks.remove(removetask)
    elif choice == 3:
        cnt = len(tasks)
        n = 0
        for n in range(0, cnt):
            print(tasks[n])
    elif choice == 4:
        print("See you next time!")
        i = 0
    else:
        print("Invalid choice.")

