from pathlib import Path
import PySimpleGUI as sg

def popup_text(filename, text, count):
    layout = [
        [sg.Multiline(text, size=(80, 25)),
         sg.Text(count)
         ]
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
    # với sự kiện event là Open và values chính là đường dẫn vừa chọn
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Open':
        # filename chính là đường dẫn đã chọn
        filename = values['-INPUT-']
        # Nếu như file tồn tại
        if Path(filename).is_file():
            try:
                # Đọc file
                with open(filename, "rt", encoding='utf-8') as f:
                    text = f.read()
                    line = text.split(" ")
                    count = str(len(line)) + " từ"
                popup_text(filename, text, count)
            except Exception as e:
                print("Error: ", e)

window.close()