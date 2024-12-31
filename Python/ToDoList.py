#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Libs
import os
import ast

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

        elif escolha.lower() == 'q':
            print('Bye Bye!')
            break

        else:
            input('ESCOLHA UMA OPÇÃO')


#Lista Pessoal
def Pessoal():
    AfazeresPessoal = []
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('''
░█▀█░█▀▀░█▀▀░█▀▀░█▀█░█▀█░█░░
░█▀▀░█▀▀░▀▀█░▀▀█░█░█░█▀█░█░░
░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
____________________________
''')
        print('Afazeres:')
        if AfazeresPessoal == []:
            PrimeiroAdd = str(input('Adicione sua primeira tarefa: (Digite exit para sair) '))
            AfazeresPessoal.append(PrimeiroAdd)
            if PrimeiroAdd == 'exit':
                ToDoList()
                break
            with open(__file__, 'r') as file:
                lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresPessoal é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresPessoal ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresPessoal no código fonte
                lines[i] = f'{indent}AfazeresPessoal = {AfazeresPessoal}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')

        else:
            #Ordem de numeração
            for i, tarefa in enumerate(AfazeresPessoal, 1):
                print(f'{i}. {tarefa}')
            print('___________________________________')
            print('[1]Adicionar [2]Remover [Q]Voltar')
            
            try:
                options = str(input(">>> "))
            except ValueError:
                continue

            if options == '1':
                adicionar = str(input('Tarefa: '))
                AfazeresPessoal.append(adicionar)
                with open(__file__, 'r') as file:
                    lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresPessoal é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresPessoal ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresPessoal no código fonte
                lines[i] = f'{indent}AfazeresPessoal = {AfazeresPessoal}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')
                

            elif options == '2':
                remover = int(input('Remover: '))
                AfazeresPessoal.pop(remover - 1)
                with open(__file__, 'r') as file:
                    lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresPessoal é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresPessoal ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresPessoal no código fonte
                lines[i] = f'{indent}AfazeresPessoal = {AfazeresPessoal}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')

            elif options.lower() == 'q':
                ToDoList()
                break
            
#Lista Faculdade
def Faculdade():
    AfazeresFaculdade = []
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('''
░█▀▀░█▀█░█▀▀░█░█░█░░░█▀▄░█▀█░█▀▄░█▀▀
░█▀▀░█▀█░█░░░█░█░█░░░█░█░█▀█░█░█░█▀▀
░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀░▀░▀▀░░▀▀▀
____________________________________
''')
        print('Afazeres:')
        if AfazeresFaculdade == []:
            PrimeiroAdd = str(input('Adicione sua primeira tarefa: (Digite exit para sair) '))
            AfazeresFaculdade.append(PrimeiroAdd)
            if PrimeiroAdd == 'exit':
                ToDoList()
                break
            with open(__file__, 'r') as file:
                lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresFaculdade é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresFaculdade ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresFaculdade no código fonte
                lines[i] = f'{indent}AfazeresFaculdade = {AfazeresFaculdade}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')

        else:
            #Ordem de numeração
            for i, tarefa in enumerate(AfazeresFaculdade, 1):
                print(f'{i}. {tarefa}')
            print('___________________________________')
            print('[1]Adicionar [2]Remover [Q]Voltar')
            
            try:
                options = str(input(">>> "))
            except ValueError:
                continue

            if options == '1':
                adicionar = str(input('Tarefa: '))
                AfazeresFaculdade.append(adicionar)
                with open(__file__, 'r') as file:
                    lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresFaculdade é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresFaculdade ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresFaculdade no código fonte
                lines[i] = f'{indent}AfazeresFaculdade = {AfazeresFaculdade}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')
                

            elif options == '2':
                remover = int(input('Remover: '))
                AfazeresFaculdade.pop(remover - 1)
                with open(__file__, 'r') as file:
                    lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresFaculdade é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresFaculdade ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresFaculdade no código fonte
                lines[i] = f'{indent}AfazeresFaculdade = {AfazeresFaculdade}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')

            elif options.lower() == 'q':
                ToDoList()
                break




#Lista Trabalho
def Trabalho():
    AfazeresTrabalho = []
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('''
░▀█▀░█▀▄░█▀█░█▀▄░█▀█░█░░░█░█░█▀█
░░█░░█▀▄░█▀█░█▀▄░█▀█░█░░░█▀█░█░█
░░▀░░▀░▀░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀▀▀
________________________________
''')
        print('Afazeres:')
        if AfazeresTrabalho == []:
            PrimeiroAdd = str(input('Adicione sua primeira tarefa: (Digite exit para sair) '))
            AfazeresTrabalho.append(PrimeiroAdd)
            if PrimeiroAdd == 'exit':
                ToDoList()
                break
            with open(__file__, 'r') as file:
                lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresTrabalho é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresTrabalho ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresTrabalho no código fonte
                lines[i] = f'{indent}AfazeresTrabalho = {AfazeresTrabalho}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')

        else:
            #Ordem de numeração
            for i, tarefa in enumerate(AfazeresTrabalho, 1):
                print(f'{i}. {tarefa}')
            print('___________________________________')
            print('[1]Adicionar [2]Remover [Q]Voltar')
            
            try:
                options = str(input(">>> "))
            except ValueError:
                continue

            if options == '1':
                adicionar = str(input('Tarefa: '))
                AfazeresTrabalho.append(adicionar)
                with open(__file__, 'r') as file:
                    lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresTrabalho é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresTrabalho ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresTrabalho no código fonte
                lines[i] = f'{indent}AfazeresTrabalho = {AfazeresTrabalho}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')
                

            elif options == '2':
                remover = int(input('Remover: '))
                AfazeresTrabalho.pop(remover - 1)
                with open(__file__, 'r') as file:
                    lines = file.readlines()

                # Encontrar a linha onde a lista AfazeresTrabalho é definida
                for i, line in enumerate(lines):
                    if line.strip().startswith('AfazeresTrabalho ='):
                        indent = line[:len(line) - len(line.lstrip())]
                        break

                # Atualizar a lista AfazeresTrabalho no código fonte
                lines[i] = f'{indent}AfazeresTrabalho = {AfazeresTrabalho}\n'

                with open(__file__, 'w') as file:
                    file.writelines(lines)
                print('Tarefas salvas no código fonte.')

            elif options.lower() == 'q':
                ToDoList()
                break

#Run
ToDoList()