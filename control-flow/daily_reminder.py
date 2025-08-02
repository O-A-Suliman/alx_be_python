task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority in ["medium", "low"]:
        reminder = f"Note: {reminder}. Consider completing it when you have free time."
print("\nReminder:", reminder)
