import PySimpleGUI

label = PySimpleGUI.Text("Type in a To-Do")
input_box = PySimpleGUI.InputText(tooltip="Enter a todo")
button = PySimpleGUI.Button("Add")
window = PySimpleGUI.Window("Simple py app", layout=[[label, input_box, button]])
window.read()
window.close()
