import json
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

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
    habit = input(Fore.CYAN + "Enter a new habit: ").strip()
    if habit in habits:
        print(Fore.RED + "Habit already exists!")
    else:
        habits[habit] = []
        print(Fore.GREEN + f"Added habit: {habit}")
        save_habits()

def mark_habit():
    show_habits()
    habit = input(Fore.CYAN + "Which habit did you complete today? ").strip()
    if habit in habits:
        habits[habit].append(Fore.GREEN + "✔ Done")
        print(Fore.YELLOW + f"Marked {habit} as completed today!")
        save_habits()
    else:
        print(Fore.RED + "Habit not found!")

def show_habits():
    if not habits:
        print(Fore.RED + "No habits found!")
    else:
        for habit, history in habits.items():
            print(Fore.MAGENTA + f"{habit}: " + Fore.GREEN + (', '.join(history) if history else "No progress yet"))

while True:
    print(Fore.BLUE + "\n📌 " + Style.BRIGHT + "Habit Tracker")
    print(Fore.YELLOW + "1. Add Habit")
    print(Fore.YELLOW + "2. Mark Habit as Done")
    print(Fore.YELLOW + "3. Show Habit History")
    print(Fore.RED + "4. Exit")

    choice = input(Fore.CYAN + "Choose an option: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        mark_habit()
    elif choice == "3":
        show_habits()
    elif choice == "4":
        print(Fore.GREEN + "Goodbye! Keep tracking your habits! 😊")
        break
    else:
        print(Fore.RED + "Invalid choice, try again!")
