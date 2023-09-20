import PySimpleGUI as sg

# Specify the path to your specific PNG file (previously converted from SVG)
png_file_path = r"C:\Users\abhilasha bisht\Downloads\Flower a transparent page background.png"
layout = [
    [sg.Text('This is a hole in the window:')],
    [sg.Image(filename=png_file_path, key='svg_image', size=(1920, 1080))],
    [sg.Button('Exit')]
]

# Set the window size to match your screen resolution
screen_width, screen_height = 1920, 1080  # Adjust these values as needed

window = sg.Window(
    'Window Title',
    layout,
    transparent_color='none',  # Set the transparent color
    no_titlebar=False,  # Remove the title bar
    grab_anywhere=True,  # Allow dragging by clicking anywhere on the window
    keep_on_top=True,
    size=(screen_width, screen_height)  # Set the window size
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
