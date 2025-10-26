import datetime

print("Daily Mood & Productivity Tracker")

mood = input("How’s your mood today? (Happy/Meh/Sad): ")
hours = input("How many hours did you code/study today? ")
lesson = input("What’s one thing you learned today?: ")
now = datetime.datetime.now().strftime("%Y-%m-%d")

entry = f"{now} | Mood: {mood} | Hours: {hours} | Lesson: {lesson}\n"

with open("tracker.txt", "a") as file:
    file.write(entry)

print("\nEntry recorded!")
print(entry)
