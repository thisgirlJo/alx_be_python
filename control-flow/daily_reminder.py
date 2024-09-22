task = input("Enter your task: ")

priority = input("Priority (high, medium, low): ")

time_bound = input("Is it task time bound? (yes or no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: ", task ," is a", priority ,"priority task that requires immediate attention today!")
        else:
            print("Reminder: " ,task ,"is a ", priority, "priority task that requires attention between today and tomorrow")
    case "medium":
        if time_bound == "yes":
            print("Reminder: " ,task, " is a" ,priority ,"priority task that requires attention within the next 2 days!" )
        else:
            print("Reminder: ", task ," is a" ,priority ,"priority task is important but doesnt require immediate attention at the moment.")
    case "low":
        if time_bound == "yes":
            print("Note: ", task, " is a", priority ,"priority task. It's not so important but do keep it in mind as you work")
        else:
            print("Note: ", task ," is a", priority ,"priority task. Consider completing it when you have free time.")
