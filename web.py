import streamlit as st
import functions
import time

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

clock = time.strftime('%b %d %Y %H:%M:%S', time.localtime())

st.title("My To-Do App")
st.subheader(clock)
st.write("This app is to increase your productivity.")


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

new_todo = st.text_input("", placeholder="New To-Do", on_change=add_todo, key="new_todo")


