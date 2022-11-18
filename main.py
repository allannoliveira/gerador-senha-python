import random
import PySimpleGUI as sg
import os

#layout
sg.theme('Dark2')
layout = [  [sg.Text('Menu')],
            [[sg.Checkbox('Senha Forte', default=True, key='checkbox1'), sg.Checkbox('Senha Numérica', key='checkbox2')]],
            [sg.OK(), sg.Cancel()]]
            

window = sg.Window('Window Title', layout)




def senhaForte():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%¨&*(){}^~?/"


    string = lower + upper + numbers + symbols
    length = int(input("Qual o tamanho para sua senha: "))
    password = "".join(random.sample(string, length))

    print(f'Sua nova senha é: {password}')

def senhaNumerica():
    i = 0
    password = []
    
    while i < 6:
        
        x = random.randint(1, 99)

        password.append(x)

        i += 1
    print (f'Sua nova senha é: {password}')










## Funcionar metodo
while True:
    event, values = window.read()
    
    if values['checkbox1']:
        ## instanciando nova janela para exibir senha
        layout2 = [
            [sg.Text(f'Sua nova senha é:  ')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
        ]     
        
        window2 = sg.Window('Window Title', layout2)
        
        ## Manter janela aberta
        
        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
       
            window['-OUTPUT-'].update(values)

        
    if values['checkbox2']:
        senhaNumerica()
        

        

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    

window.close()





def senhaForte():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%¨&*(){}^~?/"


    string = lower + upper + numbers + symbols
    length = int(input("Qual o tamanho para sua senha: "))
    password = "".join(random.sample(string, length))

    print(f'Sua nova senha é: {password}')




def senhaNumerica():
    i = 0
    password = []
    
    while i < 6:
        
        x = random.randint(1, 99)

        password.append(x)

        i += 1
    print (f'Sua nova senha é: {password}')



