def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as fp:
        todos = fp.readlines()
        return todos



def write_todos(todos,filepath="todos.txt"):
    with open(filepath,'w') as fp:
        fp.writelines(todos)
        return todos

if __name__ =="__main__":
    print("hello this is functions module")