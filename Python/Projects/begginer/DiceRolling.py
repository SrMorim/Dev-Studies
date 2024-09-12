#Libs
import random

#Lista
dice = [1, 2, 3, 4, 5, 6]

#Função
while True:
    escolha = str(input('Rolar dado? (y/n)\n>>> '))
    if escolha == 'y':
        print(random.choice(dice))
    elif escolha == 'n':
        print('Bye Bye!')
        break