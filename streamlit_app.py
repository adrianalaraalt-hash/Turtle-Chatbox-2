# streamlit_app.py
import streamlit as st
from datetime import date
from src.core import create_task, mark_done, list_tasks

st.title("🎓 Student Task Manager (Vertical Slice)")

# Keep tasks across reruns
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Inputs ---
task_name = st.text_input("Task name")
due_dt = st.date_input("Due date", value=date.today())

# Button to add a task
if st.button("Add Task"):
    if task_name.strip():
        new_task = create_task(task_name, str(due_dt))
        st.session_state.tasks.append(new_task)
        st.success(f"Added: {task_name}")
    else:
        st.warning("Please enter a task name.")

st.divider()

# --- Display & mark done ---
st.subheader("Your tasks")
if not st.session_state.tasks:
    st.info("No tasks yet. Add one above!")
else:
    # Show each task with a checkbox to mark done
    for i, t in enumerate(st.session_state.tasks):
        checked = st.checkbox(
            f"{t['name']} — due {t['due']}",
            value=t["done"],
            key=f"done_{i}"
        )
        # Keep the underlying dict in sync with the checkbox
        st.session_state.tasks[i]["done"] = bool(checked)

    # Pretty list below
    st.write("—")
    for line in list_tasks(st.session_state.tasks):
        st.write(line)

# Optional reset
if st.button("Clear all tasks"):
    st.session_state.tasks = []
    st.warning("Cleared all tasks.")
