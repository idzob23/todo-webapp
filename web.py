import streamlit as st
import functions

print("ilija")
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo']=''  #clean the input box


st.title("My Todo App")
st.subheader("This is my todo app..")
st.write("This app is to increase your productivity")

todos = functions.get_todos()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()   #refresh the page

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


#st.session_state
