my_schedule = []

def added_to_schedule(task):
    my_schedule.append(task)
    return f"Added {task} to your today's schedule!"

def your_schedule():
    if my_schedule:
        return "Your schedule for today is: " + ", ".join(my_schedule) + "."
    else:
        return "You have no tasks in your schedule for today."
