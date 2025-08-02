task=input("Enter your task: ")
Priority=input("Priority (high/medium/low): ").strip()
time=input("Is it time-bound? (yes/no): ").strip()
match time:
    case "yes":
            print(f"Reminder: '{task}' is a {Priority} priority task that requires immediate attention today!")
    case "no":
        print(f"Note: '{task}' is a {Priority} priority task. Consider completing it when you have free time.")
    case _:
          print("Message unknown")
