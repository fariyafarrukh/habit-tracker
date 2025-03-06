import json
import streamlit as st

FILE_NAME = "habits.json"

# Habits کو لوڈ کرنے کا فنکشن
def load_habits():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Habits کو سیو کرنے کا فنکشن
def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)

# Habits کو لوڈ کریں
habits = load_habits()

# Streamlit UI  
st.title("📌 Habit Tracker")

# نیا habit شامل کرنے کے لیے  
new_habit = st.text_input("Enter a new habit:")
if st.button("Add Habit"):
    if new_habit:
        if new_habit in habits:
            st.error("❌ Habit already exists!")
        else:
            habits[new_habit] = []
            save_habits(habits)
            st.success(f"✅ Added habit: {new_habit}")
    else:
        st.warning("⚠ Please enter a habit!")

# Habit مکمل کرنے کے لیے
st.subheader("Mark Habit as Done")
selected_habit = st.selectbox("Which habit did you complete today?", [""] + list(habits.keys()))
if st.button("Mark as Done"):
    if selected_habit:
        habits[selected_habit].append("✔ Done")
        save_habits(habits)
        st.success(f"✅ Marked '{selected_habit}' as completed today!")
    else:
        st.warning("⚠ Please select a habit!")

# Habits کو دکھانے کے لیے
st.subheader("📜 Habit History")
if habits:
    for habit, history in habits.items():
        st.write(f"**{habit}:** {' | '.join(history) if history else 'No progress yet'}")
else:
    st.info("No habits found! Start adding new habits.")


