import PySimpleGUI
import function

label = PySimpleGUI.Text("Type in a To-Do")
input_box = PySimpleGUI.InputText(tooltip="Enter a todo", key="todo")
button = PySimpleGUI.Button("Add")
window = PySimpleGUI.Window("Simple py app", layout=[[label, input_box, button]], font=("Helvetica", 20))

while True:
    event, value = window.read()
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
        case PySimpleGUI.WINDOW_CLOSED:
            break
window.close()
