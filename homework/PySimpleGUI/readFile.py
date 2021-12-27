from pathlib import Path
import PySimpleGUI as sg

def popup_text(filename, text):
    layout = [
        [sg.Multiline(text[i]) for i in range(len(text))]
    ]
    win = sg.Window(filename, layout, modal=True, finalize=True)
    while True:
        event, values = win.read()
        if event == sg.WINDOW_CLOSED:
            break
    win.close()

sg.set_options(font=("Microsoft JhengHei", 16))

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))),
        sg.Button("Open"),
    ]
]

window = sg.Window('Home', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Open':
        filename = values['-INPUT-']
        if Path(filename).is_file():
            try:
                with open(filename, "rt", encoding='utf-8') as f:
                    text = f.read()
                    line = text.split(".")
                popup_text(filename, line)
            except Exception as e:
                print("Error: ", e)

window.close()