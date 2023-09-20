import PySimpleGUI as sg
import webview
import os

layout = [
    [sg.Text('This is a hole in the window:')],
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

# Function to load and display an SVG file using pywebview
def load_svg_file():
    # Use double backslashes in the file path
    webview.create_window('SVG Viewer', "C:\\Users\\abhilasha bisht\\Downloads\\ice-cream-svgrepo-com.svg", width=800, height=600)
    webview.start()

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Go':
        load_svg_file()

window.close()
