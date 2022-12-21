import os
from playsound import playsound

while True:
 print('Roleta Russa')
 escolha = int(input('Digite um Numero de 1 a 6: '))

 if escolha == 2:
    acao = print('Bang!')
    break
 else: 
    os.system('cls')
    playsound('reload.mp3')