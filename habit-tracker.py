import json

FILE_NAME = "habits.json"

try:
    with open(FILE_NAME, "r") as file:
        habits = json.load(file)
except FileNotFoundError:
    habits = {}

def save_habits():
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)

def add_habit():
    habit = input("Enter a new habit: ").strip()
    if habit in habits:
        print("Habit already exists!")
    else:
        habits[habit] = []
        print(f"Added habit: {habit}")
        save_habits()

def mark_habit():
    show_habits()
    habit = input("Which habit did you complete today? ").strip()
    if habit in habits:
        habits[habit].append("✔ Done")
        print(f"Marked {habit} as completed today!")
        save_habits()
    else:
        print("Habit not found!")

def show_habits():
    if not habits:
        print("No habits found!")
    else:
        for habit, history in habits.items():
            print(f"{habit}: {', '.join(history) if history else 'No progress yet'}")

while True:
    print("\n📌 Habit Tracker")
    print("1. Add Habit")
    print("2. Mark Habit as Done")
    print("3. Show Habit History")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        mark_habit()
    elif choice == "3":
        show_habits()
    elif choice == "4":
        print("Goodbye! Keep tracking your habits! 😊")
        break
    else:
        print("Invalid choice, try again!")
