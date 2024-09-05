#Libs
import os

def GamesOptions():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''' 
    ░█▀▀░█▀█░█▄█░█▀▀░█▀▀
    ░█░█░█▀█░█░█░█▀▀░▀▀█
    ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀
        Pick up one game!
    ''')
        print('[1]Guess the number\n[2]Hangman Game\n[X]Coming soon...\n[0]Back')
        SelectGame = int(input('>>> '))

        if SelectGame == 1:
            GuessNumberGame()
            break
        elif SelectGame == 2:
            HangmanGame()
            break
        elif SelectGame == 0:
            TerminalMenu()
            break

def GuessNumberGame():
    import random
    global GTNScore

    guess = 0
    number = random.randint(1,150)
    point = 100
    attempts = 10
    GTNScore = point

    input('You only have 10 attempts, as you make more mistakes, the discounted score will be higher ')
    input('Are you ready???')

    while guess != number:
        guess = int(input("What's the number?: "))
        attempts -= 1
        print(number)
        
        if attempts == 0 or point == 0:
            input('Game Over!')
            GamesOptions()
            break
        
        if guess > number:
            print('less')
            point -= 1
            print(point)
            print(attempts)
        elif guess < number:
            print('more')
            point -= 1
            print(point)
            print(attempts)

        if guess > number and attempts <= 6:
            print('less')
            point -= 5
            print(point)
            print(attempts)
        elif guess < number and attempts <= 6:
            print('more')
            point -= 5
            print(point)
            print(attempts)

        if guess > number and attempts <= 4:
            print('less')
            point -= 10
            print(point)
            print(attempts)
        elif guess < number and attempts <= 4:
            print('more')
            point -= 10
            print(point)
            print(attempts)

    if guess == number:
        print('Congrats, you found the number!\nyour final score:', point)
        input('Continue?')
        GamesOptions()
        

        

















def TotalScore():
    print("""
░█▀▀░█▀▀░█▀█░█▀▄░█▀▀
░▀▀█░█░░░█░█░█▀▄░█▀▀
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
See you total score here.
""")
    print(f'Guess the number:{GTNScore}\nTotal:{GTNScore}')


#Welcome menu!
def TerminalMenu():
    while True:
        print(''' 
        ░▀█▀░█▀▀░█▀▄░█▄█░▀█▀░█▀█░█▀█░█░░░░░█▀▀░█▀█░█▄█░█▀▀░█
        ░░█░░█▀▀░█▀▄░█░█░░█░░█░█░█▀█░█░░░░░█░█░█▀█░█░█░█▀▀░▀
        ░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀
        Play mini-games to earn points! How far can you go?
        ''')
        print('[1]Start\n[2]Score\n[0]Exit')
        choose = int(input('>>> '))

        if choose == 1:
            GamesOptions()
            break
        elif choose == 2:
            TotalScore()
            break
        elif choose == 0:
            print('bye bye!')
            break
        else:
            input('please, select only the options.')  


#Run
TerminalMenu()