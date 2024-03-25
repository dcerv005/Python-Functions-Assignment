activities= []
duration= []

def activities_done(): #Task 1
    global activities
    global duration
    num_of_activites= int(input("How many activites are you logging in today? "))
    for x in range(num_of_activites):
        activities.append(input(f'Which is activity number {x+1}? ').lower())
        duration.append(input("How long did this activity take?(in minutes) "))
    #print(activities)
    #print(duration)

def calories_burned():#Task 2
    global activities
    global duration
    burned_calories = []
    for activity in activities:
        total_calories_burned = float(duration[activities.index(activity)])*3.5
        burned_calories.append(total_calories_burned)
    #print(burned_calories)
    return burned_calories

def summary():#Task 3
    global activities
    global duration
    new_list=calories_burned()
    for x in range(len(activities)):
        print(f"Activity {x+1} was: {activities[x]}. It took {duration[x]} minute(s) and burned {new_list[x]} calorie(s)")


activities_done()
calories_burned()
summary()