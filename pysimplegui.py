from netmiko import ConnectHandler
import PySimpleGUI as sg

sg.theme('DarkBlue16')
sg.set_options(font = 'Calibri 16')

layout = [
    [sg.Text('Network Automation Demo')], 
    [sg.Text('Enter your username'), sg.Input(size=(30,1), pad=(1,0))], 
    [sg.Text('Enter your password'), sg.Input(size=(30,1), pad=(4,0))], 
    [sg.Text('Enter the device'), sg.Input(size=(30,1), pad=(42,0))], 
    [sg.Text('Select Output'), sg.Combo(['Show Interfaces','Show CDP Neighbors','Show Switch Detail', 'Show Device Version', 'Show Boot', 'Show License Summary', 'Directory Flash'], pad=(61,0), size=(29,1))],
    [sg.Button("SUBMIT"), sg.Button('CLOSE')]]

window = sg.Window("Network Automation Project", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break

    if event == 'SUBMIT':
        cisco1 = {
    "device_type": "cisco_ios",
    "host": values[2],
    "username": values[0],
    "password": values[1],}

    if values[3] == 'Show Interfaces':
        command = "show int status"
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
        sg.Print(output)

    if values[3] == 'Show CDP Neighbors':
        command = "show cdp neighbors"
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
        sg.Print(output)

    if values[3] == 'Show Switch Detail':
        command = "show switch detail"
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
        sg.Print(output)
        
    if values[3] == 'Show Device Version':
        command = "show version"
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
        sg.Print(output)  

    if values[3] == 'Show Boot':
        command = "show boot system"
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
        sg.Print(output) 

    if values[3] == 'Show License Summary':
        command = "show license summary"
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
        sg.Print(output) 

    if values[3] == 'Directory Flash':
        window_1 = sg.Window('Amount of Switches', [
            [sg.T('Enter the amount of switches')], 
            [sg.Input()],
            [sg.Button('SUBMIT'), sg.Button('CLOSE')]], disable_close=True)

        while True:
                event_1, values_1 = window_1.read()

                if event_1 == sg.WIN_CLOSED or event_1 == 'CLOSE':
                    break

                if event_1 == 'SUBMIT':
                    for i in range(1,int(values_1[0])+1):
                        command = "dir flash-" + str(i) + ":"
                        with ConnectHandler(**cisco1) as net_connect:
                            output = net_connect.send_command(command)
                        sg.Print(output)

        window_1.close()
         
window.close()
