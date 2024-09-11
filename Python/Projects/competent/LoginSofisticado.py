#Login sofisticado


class Cliente:
    def __init__(self, user, email, senha):
        self.user = user
        self.email = email
        self.senha = senha


#Login Menu
def LoginSofisticado():
    ClientesCadastrados = []
    while True:
        print('''
        ░█░░░█▀█░█▀▀░▀█▀░█▀█
        ░█░░░█░█░█░█░░█░░█░█
        ░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀
        ____________________
        ''')
        print('[1]Login\n[2]Registrar')
        escolha = int(input('>>> '))
        #Escolhas
        if escolha == 1:
            user = str(input('user\n> '))
            login = str(input('Login\n> '))
            senha = str(input('senha\n>'))
            if login and senha == ClientesCadastrados(user,email,senha):
                print('Acesso Liberado!')
                break
            else:
                print('Tente Novamente...')

        elif escolha == 2:
            user = str(input('qual seu usuario?\n>'))
            email = str(input('qual seu email?\n>'))
            senha = str(input('qual sua senha?\n>'))
            ClienteNovo = Cliente(user, email, senha)
            ClientesCadastrados = ClienteNovo
            
        

#run
LoginSofisticado()