import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%¨&*(){}^~?/"


string = lower + upper + numbers + symbols
length = int(input("Qual o tamanho para sua senha: "))
password = "".join(random.sample(string, length))

print(f'Sua nova senha é: {password}')

