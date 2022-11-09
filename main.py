import random

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

menu()

userinput = int(input('Digite o valor para criar sua senha nova: '))

if userinput == 1:
    senhaForte()
    
elif userinput == 2:
    senhaNumerica()

else:
    print('Opção inválida ')
