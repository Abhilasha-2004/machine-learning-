import PySimpleGUI as sg

layout = [
    [sg.Text('This is a hole in the window:')],
    [sg.Text(' ', size=(1920, 1080), background_color='white')],
    [sg.Button('Go'), sg.Button('Exit')]
]

# Set the window size to match your screen resolution
screen_width, screen_height = 1920, 1080  # Adjust these values as needed

window = sg.Window(
    'Window Title',
    layout,
    transparent_color='white',  # Set the transparent color
    no_titlebar=False,  # Remove the title bar
    grab_anywhere=True,  # Allow dragging by clicking anywhere on the window
    keep_on_top=True,
    size=(screen_width, screen_height)  # Set the window size
)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
