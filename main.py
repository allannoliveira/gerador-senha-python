import random
import PySimpleGUI as sg
import os

#layout
sg.theme('Dark2')
layout = [  [sg.Text('Menu')],
            [sg.Text('(1) Senhas fortes')],
            [sg.Text('(2) Senhas fracas ')],
            [sg.Text('Digite sua escolha'), sg.InputText()],
            [sg.Text(f'Sua nova senha é:  ')],
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

while True:
    event, values = window.read()
    if values == 1:
        senhaForte()
    elif values == 2:
        senhaNumerica()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

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



def menu():
    print(''' Menu
    (1) - Senhas fortes
    (2) - Senha Numérica
    ''')


