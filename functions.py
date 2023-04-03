FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read the text file and return
        the list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo_list, filepath=FILEPATH):
    """ Write the list items in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_list)

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # print(f"{feet} feet and {inches} inches is equal to {meters} meters.")
    return meters




# This will be executed in both cases (run functions.py or main141.py)


#print("Hello from functions")
#print(__name__)
# This will be executed only if run functions.py directly
# cannot be executed if you import functions into main141.py
if __name__ == "__main__":
    print("Hello")
    print(get_todos())