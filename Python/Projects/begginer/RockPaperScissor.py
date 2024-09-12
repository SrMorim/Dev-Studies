#Libs
import random

#Menu
print('''
░█▀▄░█▀█░█▀▀░█░█░░░█▀█░█▀█░█▀█░█▀▀░█▀▄░░░█▀▀░█▀▀░▀█▀░█▀▀░█▀▀░█▀█░█▀▄
░█▀▄░█░█░█░░░█▀▄░░░█▀▀░█▀█░█▀▀░█▀▀░█▀▄░░░▀▀█░█░░░░█░░▀▀█░▀▀█░█░█░█▀▄
░▀░▀░▀▀▀░▀▀▀░▀░▀░░░▀░░░▀░▀░▀░░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀
____________________________________________________________________
''')

#Escolha Player
escolha = int(input('Escolha:\n[1]🪨\n[2]📄\n[3]✂️\n>>> '))

if escolha == 1:
    print('Sua jogada: 🪨')
elif escolha == 2:
    print('Sua jogada: 📄')
elif escolha == 3:
    print('Sua jogada: ✂️')
else:
    print('Escolha uma das jogadas')

#Escolha CPU
CPUPlayer = [1, 2 , 3]
escolhaCPU = random.choice(CPUPlayer)
if escolhaCPU == 1:
    print('CPU jogou: 🪨')
elif escolhaCPU == 2:
    print('CPU jogou: 📄')
elif escolhaCPU == 3:
    print('CPU jogou: ✂️')

#Regras jogo
#Pedra
if escolhaCPU == escolha:
    print('Empate!')
elif escolhaCPU == 2 and escolha == 1:
    print('Você Perdeu...')
elif escolhaCPU == 3 and escolha == 1:
    print('Você Ganhou!')
#Papel
elif escolhaCPU == 1 and escolha == 2:
    print('Você Ganhou!')
elif escolhaCPU == 3 and escolha == 2:
    print('Você Perdeu...')
#Tesoura
elif escolhaCPU == 1 and escolha == 3:
    print('Você Perdeu!')
elif escolhaCPU == 2 and escolha == 3:
    print('Você Ganhou!')
