import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("NO")]]
window = sg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "NO":
        break

window.close()