import PySimpleGUI as sg
import time
import pyautogui
#import os
#import shutil

# Define the window's contents
layout = [[sg.Text("Destinasjonen til filene du vil exportere")],
          [sg.Input(key='-INPUT-')],
          [sg.Text("Destinasjonen filene skal exporteres til")],
          [sg.Input(key="-INPUT2-")],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Start'), sg.Button('Close')]]

# Create the window
window = sg.Window('File Exporter', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    elif event == "Start":
        origin = values["-INPUT-"]
        print(origin)
        destination = values["-INPUT2-"]
        print(destination)
        os.listdir(origin)
        shutil.move(origin, destination)

    # Output a mess
    # age to the window
    window['-OUTPUT-'].update('Transfering to ' + values['-INPUT2-'] + " Prosess started")

# Finish up by removing from the screen
window.close()
