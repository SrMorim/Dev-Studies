#Libs
import os

#Menu ToDoList
def ToDoList():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
░▀█▀░█▀█░░░█▀▄░█▀█░░░█░░░▀█▀░█▀▀░▀█▀
░░█░░█░█░░░█░█░█░█░░░█░░░░█░░▀▀█░░█░
░░▀░░▀▀▀░░░▀▀░░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░░▀░
____________________________________
''')
        print('[1]Pessoal\n[2]Faculdade\n[3]Trabalho\n[Q]Sair')
        try:
            escolha = str(input('>>> '))
        except ValueError:
            continue
        if escolha == '1':
            Pessoal()
            break
        elif escolha == '2':
            Faculdade()
            break
        elif escolha == '3':
            Trabalho()
            break
        elif escolha == 'Q' or 'q':
            print('Bye Bye!')
            break
        else:
            input('ESCOLHA UMA OPÇÃO')


#Lista Pessoal
def Pessoal():
    TotalPessoal = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('''
░█▀█░█▀▀░█▀▀░█▀▀░█▀█░█▀█░█░░
░█▀▀░█▀▀░▀▀█░▀▀█░█░█░█▀█░█░░
░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
''')
        if TotalPessoal == 0:
            add = str(input("Adicione sua primeira tarefa!"))







#Lista Faculdade
def Faculdade():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('''
░█▀▀░█▀█░█▀▀░█░█░█░░░█▀▄░█▀█░█▀▄░█▀▀
░█▀▀░█▀█░█░░░█░█░█░░░█░█░█▀█░█░█░█▀▀
░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀░▀░▀▀░░▀▀▀
''')
        












#Lista Trabalho
def Trabalho():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('''
░▀█▀░█▀▄░█▀█░█▀▄░█▀█░█░░░█░█░█▀█
░░█░░█▀▄░█▀█░█▀▄░█▀█░█░░░█▀█░█░█
░░▀░░▀░▀░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
''')







#Run
ToDoList()