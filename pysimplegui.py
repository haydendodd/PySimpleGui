import PySimpleGUI as sg
from netmiko import ConnectHandler

sg.theme('DarkBlue16')
sg.set_options(font = 'Calibri 16')

layout = [
    [sg.Text('Network Automation Demo', key='Status')], 
    [sg.Text('Enter your username'), sg.Input(size=(20,1), pad=(1,0))], 
    [sg.Text('Enter your password'), sg.Input(size=(20,1), pad=(2,0))], 
    [sg.Text('Enter the device'), sg.Input(size=(20,1), pad=(33,0))], 
    [sg.Text('Select Output'), sg.Combo(['Show Interfaces','Show CDP Neighbors','Show Clock'], pad=(50,0))],
    [sg.Button("OK"), sg.Button('CLOSE')]]

window = sg.Window("Network Automation Project", layout)

while True:
    event, values =  window.read()
    if event == sg.WIN_CLOSED or event == "CLOSE":
        break
    if event == "OK":
     sg.Print(values[0])

window.close()