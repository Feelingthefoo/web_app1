FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Fetch the existing to-dos from a specified file.

    Parameters:
    - filepath (str): Path to the file containing the to-dos. Default is "todos.txt".

    Returns:
    - list: A list of to-dos extracted from the file.
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """
    Overwrites the specified file with the given list of to-dos.

    Parameters:
    - todos (list): List of to-dos to be written to the file.
    - filepath (str): Path to the file where the to-dos will be written. Default is "todos.txt".
    """
    with open(filepath, "w") as file:
        file.writelines(todos)