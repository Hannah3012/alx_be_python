while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

priority = input("Priority (high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that still requires attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Fit it into your schedule soon.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but is time-bound. Don't let it slip!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")
