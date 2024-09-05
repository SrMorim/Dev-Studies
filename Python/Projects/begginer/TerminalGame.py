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
    while True:
        print('''
░█▀▀░█░█░█▀▀░█▀▀░█▀▀░░░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄
░█░█░█░█░█▀▀░▀▀█░▀▀█░░░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄
░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀
            Guess the number!
              ''')
        os.system('cls' if os.name == 'nt' else 'clear')
        import random
        global GTNtotal

        guess = 0
        number = random.randint(1, 100)
        point = 100
        descpoint = 0
        GTNtotal = point - descpoint
        attempts = 10

        input('You only have 10 attempts, as you make more mistakes, the discounted score will be higher, number between 1 and 100.')
        input('Are you ready???')

        while guess != number:
            guess = int(input("What's the number?: "))
            attempts -= 1
            
            if attempts == 0:
                print('The number was:', number)
                input('Game Over!')
                GamesOptions()
                break
            
            if guess > number:
                print('less')
                descpoint += 2
            elif guess < number:
                print('more')
                descpoint += 2

            if attempts <= 6:
                if guess > number:
                    print('less')
                    descpoint += 5
                elif guess < number:
                    print('more')
                    descpoint += 5

            if attempts <= 4:
                if guess > number:
                    print('less')
                    descpoint += 10
                elif guess < number:
                    print('more')
                    descpoint += 10

            GTNtotal = point - descpoint
            print(f"Points: {GTNtotal}, Attempts left: {attempts}")

        if guess == number:
            print('Congrats, you found the number!\nYour final score:', GTNtotal)
            input('Continue?')

            GamesOptions()
            break
        
def HangmanGame():
    import random
    global HMpoint
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
    ░█░█░█▀█░█▀█░█▀▀░█▄█░█▀█░█▀█
    ░█▀█░█▀█░█░█░█░█░█░█░█▀█░█░█
    ░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀
    Welcome to Hangman Game!
    ''')

        word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
        word = random.choice(word_list)
        guessed_letters = []
        attempts = 6
        HMpoint = 100

        while attempts > 0:
            print("\nAttempts left:", attempts)
            print("Guessed letters:", guessed_letters)
            print("Word:", ''.join([letter if letter in guessed_letters else '_' for letter in word]))

            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess.isalpha() and len(guess) == 1:
                guessed_letters.append(guess)
                if guess in word:
                    print("Correct guess!")
                    if all(letter in guessed_letters for letter in word):
                        print("Congratulations, you guessed the word!")
                        break
                else:
                    print("Wrong guess!")
                    attempts -= 1
                    HMpoint -= 10
            else:
                print("Invalid input! Please enter a single letter.")

        if attempts == 0:
            print("Game over! The word was:", word)

        print("Total points:", HMpoint)
        input("Press Enter to continue...")
        GamesOptions()
        break









def TotalScore():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
    ░█▀▀░█▀▀░█▀█░█▀▄░█▀▀
    ░▀▀█░█░░░█░█░█▀▄░█▀▀
    ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀
    See you total score here.
    """)
        print('_______________________________')
        print('Guess the number:', GTNtotal)
        print('Hungman Game:', HMpoint)
        print('_______________________________')
        print('total:', GTNtotal + HMpoint)
        input('')
        TerminalMenu()
        break


#Welcome menu!
def TerminalMenu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''' 
        ░▀█▀░█▀▀░█▀▄░█▄█░▀█▀░█▀█░█▀█░█░░░░░█▀▀░█▀█░█▄█░█▀▀░█
        ░░█░░█▀▀░█▀▄░█░█░░█░░█░█░█▀█░█░░░░░█░█░█▀█░█░█░█▀▀░▀
        ░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀
        Play mini-games to earn points! How far can you go?
        ''')
        print('[1]Start\n[2]Score (select after played all games)\n[0]Exit')
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