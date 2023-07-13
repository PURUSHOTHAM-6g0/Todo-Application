import os.path

import PySimpleGUI as sg
from functions import get_todos,write_todos
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as fp:
        pass




sg.theme("DarkBlue17")
label = sg.Text("Enter a todo")
input_text = sg.InputText(tooltip="write todo ", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=get_todos(),key="todos",
                      enable_events=True,size=(45,10))
edit_button = sg.Button("edit")
window = sg.Window('TODO',
                   layout=[[label], [input_text, add_button,],
                           [list_box],[complete_button, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=[''][0])

        case "edit":
            try:
                todo1 = values['todos'][0]
                todo2 = values['todo']+"\n"

                todos = get_todos()
                index = todos.index(todo1)
                todos.pop(index)
                todos.insert(index, todo2)
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=('Helvetica', 15))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                todos = get_todos()
                tobe_remove = values['todos'][0]
                todos.remove(tobe_remove)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=['Deleted 😃'][0])
            except IndexError:
                sg.popup("Please select an item first",font=('Helvetica', 15))


        case sg.WIN_CLOSED:

            break


window.close()

