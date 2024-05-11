FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read todos as list from a file with a default filepath named todos.txt """
    with open(filepath, 'r') as mfile_local:
        todos_local = mfile_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write to-dos items list in text file with default name todos.txt """
    with open(filepath,'w') as mfile:
        mfile.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())