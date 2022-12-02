from netmiko import ConnectHandler
import PySimpleGUI as sg
import json

sg.theme('DarkBlue16')
sg.set_options(font = 'Calibri 16')

layout = [
    [sg.Text('Network Automation Demo')], 
    [sg.Text('Enter your username'), sg.Input(size=(30,1), pad=(1,0))], 
    [sg.Text('Enter your password'), sg.Input(size=(30,1), pad=(4,0))], 
    [sg.Text('Enter the device'), sg.Input(size=(30,1), pad=(42,0))], 
    [sg.Text('Select Output'), sg.Combo(['Show Interfaces','Show CDP Neighbors','Show Switch Detail', 'Show Device Version', 'Show Boot', 'Show License Summary', 'Directory Flash', 'Other Command'], pad=(61,0), size=(29,1))],
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
        command = "show ip int brief"
        with ConnectHandler(**cisco1) as net_connect:
            interfaces = net_connect.send_command(command, use_textfsm=True)
        sg.Print(json.dumps(interfaces, indent=2))
        #for interface in interfaces:
            #if interface['proto'] == 'down':
                #sg.Print(f"{interface['intf']} is down!")

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
            devices = net_connect.send_command(command, use_textfsm=True)
        for device in devices:
            global hardware
            hardware = device['hardware']
        sg.Print(output)

    if values[3] == 'Show Boot':
        if hardware == ['IOSv']:
            command = "show boot"
            with ConnectHandler(**cisco1) as net_connect:
                output = net_connect.send_command(command)
            sg.Print(output) 
        else:
            sg.Print('This did not work')

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
                    if hardware == ['IOSv']:
                        #for i in range(1,int(values_1[0])+1):
                            #command = "dir flash-" + str(i) + ":"
                            #with ConnectHandler(**cisco1) as net_connect:
                                #output = net_connect.send_command(command)
                            #sg.Print(output)
                        sg.Print('dir flash:')
                    else:
                        sg.Print('this did not work')

        window_1.close()

    if values[3] == 'Other Command':
        window_2 = sg.Window('Enter the Command', [
            [sg.T('Enter the command you would like to run')], 
            [sg.Input()],
            [sg.Button('SUBMIT'), sg.Button('CLOSE')]], disable_close=True)

        while True:
                event_2, values_2 = window_2.read()

                if event_2 == sg.WIN_CLOSED or event_2 == 'CLOSE':
                    break

                if event_2 == 'SUBMIT':
                    command = values_2[0]
                    with ConnectHandler(**cisco1) as net_connect:
                        output = net_connect.send_command(command)
                    sg.Print(output)

        window_2.close()

window.close()
