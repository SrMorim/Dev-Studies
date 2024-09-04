# Scripts em Python para registrar meu nível de aprendizado em um só arquivo.

#Libs usadas
import math
import random

#> Nível Básico

def Login():
#Elabore um programa que verifica se o usuário digitou a senha correta. Mostre a mensagem "senha incorreta" ou "Acesso liberado". Supondo que a senha correta seja 123.
    Senha = '123'

    login = str(input('Digite a senha: '))

    if login == Senha:
        print('Acesso liberado.')
    else:
        print('Acesso Negado.')

def MaiorQCem():
#Faça um programa que leia um valor numérico e mostre uma mensagem
    num1 = float(input('Digite o numero: '))

    if (num1 >= 100):
        print ('número maior que cem')

    elif (num1 <= 100):
        print ('numero é menor que cem')

    elif (num1 == 100):
        print ('os dois sao iguais')
    else:
        print('digire o número')

def NumerosIguais():
#Faça um programa que leia dois valores quaisquer e mostre o maior deles ou mostre a mensagem "os valores são iguas"
    num1 = float(input('primeiro numero: '))
    num2 = float(input('Segundo numero: ' ))

    if (num2 > num1):
        print ('segundo numero é maior que o primeiro numero')

    if (num1 > num2):
        print ('primeiro numero é maior que o segundo numero')

    if (num1 == num2):
        print ('os dois sao iguais')

def NecessidadeDAgua():
# A água é um nutriente essencial. sem ela, o corpo não pode funcionar com perfeição. Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo. A dose ideal, ou seja, a necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.
    kg = float(input('Quantos quilos você tem?: '))
    cal = kg * 0.03
    print(f'Você precisa tomar {cal} litros de água')

def ImparPar():
#Elabore um programa que verifica se o valor inteiro fornecido pelo usuário é impar ou par.;
    num = int(input('Digite um número: '))

    if (num%2) == 0:
        resto = num%2
        print(f"Par (número {num} e seu resto é: {resto})")
    else:
        print("Ímpar")

def AprovadoReprovado():
#Programa que calcule a média aritmética de um aluno que realizou duas avaliações. Além do valor da média, inclua na tela de saída uma das mensagens: "Aluno aprovado" ou "Aluno reprovado". Considere que o aluno será aprovado com a média maior ou igual a 5.

    nota = int(input('Digite a nota do aluno: '))
    nota2 = int(input('Digite a segunda nota do aluno: '))

    media = (nota + nota2)/2

    if (media >= 5):
        print ('APROVADO')

    elif (media <= 5):
        print ('REPROVADO')

    elif (media == 5):
        print ('APROVADO')
    else:
        print('digite o número')

def ValorDVenda():
#Recebe os valores de compra e de venda, lê os valores, converta para float e atribui à variavel.
    vl_compra = float(input('Digite o valor de compra: '))
    vl_venda = float(input('Digite o valor de venda: '))
    if vl_compra < vl_venda:
        print(f'Lucro, o valor da compra foi {vl_compra} e o valor da venda foi {vl_venda}, lucro foi de {vl_venda - vl_compra}')
    elif vl_compra > vl_venda:
        print(f'Prejuízo. o valor da compra foi {vl_compra} e o valor da venda foi {vl_venda}, o valor de prejuízo foi de {vl_compra - vl_venda}')
    else:
        print('Empate')
    
def AnoDeNascimento():
#Calcule o programa que leia o ano de nascimento de uma pessoa e mostre se ela tem idade para votar (16 anos ou mais). Mostre a imagem informando a situação.
    idade = int(input('Digite a sua idade: '))
    if (idade >= 16 and idade <= 17):
        print(f'Você tem {idade} anos, pode votar')
    elif idade >= 18:
        print(f'Você tem {idade} anos, pode votar e tirar CNH')
    else:
        print(f'Você tem {idade} anos, não pode votar')
        
def CalculoRaiz():
# Projete o programa que calcule as raízes de uma equação do segundo grau. O usuário fornecerá os valores dos coeficientes a, b e c. Levando em consideração  a análise da existencia de raízes nos reais.; Se delta for igual a zero, existem duas raízes iguais; se delta for igual a zero, existem duas raízes iguais; se delta for maior que zero, existem duas raizes reais e distintas. 
    a = float(input("Digite o valor do coeficiente a: "))
    b = float(input("Digite o valor do coeficiente b: "))
    c = float(input("Digite o valor do coeficiente c: "))

    delta = b**2 - 4*a*c
    print(delta)
    if (a == 0 or b == 0 or c == 0):
        print("O coeficiente a não pode ser zero.")
    elif delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são {raiz1} e {raiz2}")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz dupla: {raiz}")
    else:
        print("A equação não possui raízes reais.")

def Hypotenuse():
    a = int(input("Digite o valor do cateto a: "))
    b = int(input("Digite o valor do cateto b: "))
    c = (a**2 + b**2)**0.5
    print(f"O valor da hipotenusa é {c}")

def Currency():
#Crie um programa currency.py que pergunte ao usuário o valor que ele tem em pesos, soles e reais e calcule o total em USD.
    pesos = float(input("Digite o valor em pesos: "))
    soles = float(input("Digite o valor em soles: "))
    reais = float(input("Digite o valor em reais: "))
    total = pesos*0.0011 + soles*0.28 + reais*0.18
    print(f"O total em USD é {total:.2f}")

def CaraCoroa():
    num = random.randint(0,1)
    if num > 0.5:
        print('Cara')
    else:
        print('coroa')

def bola8():
    pergunta = input('o que te preocupas?:      ')
    respostas = ["Sim, Definitivamente", "Sem dúvidas", "Responder nebuloso, tente novamente.", "Pergunte novamente mais tarde.", 'Melhor não contar agora', 'Minhas fontes dizem que não.', 'Perspectiva não tão boa.', 'Muito duvidoso', 'Melhor não', 'Definitivamente não' ]
    print('Bola 8: ', random.choice(respostas))

def cyclone():
    altura = int(input('qual sua altura em cm?: '))
    credito = int(input('quantos créditos você tem?: '))

    if (credito >= 10 and altura >= 137):
        print('Aproveite o passeio!') 
    elif (credito >= 10 and altura <=136):
        print('Você não é alto o suficiente para entrar')
    elif (credito <= 9 and altura >= 137):
        print('Você não tem créditos suficientes')
    else:
        print('nenhum dos requisitos')

def ChapeuSeletor():
    #Casas
    grifinoria = 0
    cornival = 0
    lufalufa = 0
    sonserina = 0
    #Questão 1
    print('Q1)Voce gosta do amanhecer ou crepúsculo?\n1)Amanhecer\n2)Crepúsculo')
    rq1 = int(input('Escolha: '))

    if rq1 == 1:
        grifinoria += 1
        cornival += 1
    elif rq1 == 2:
        lufalufa += 1
        sonserina += 1
    else:
        print('entrada inválida')

    print('')
    # Questão 2
    print('Q2) Quando eu morrer, quero que as pessoas se lembrem de mim como:\n1)O bom\n2)O Grande\n3)O Sábio\n4)O Ousado')
    rq2 = int(input('Escolha: '))

    if rq2 == 1:
        lufalufa += 2
    elif rq2 == 2:
        sonserina += 2
    elif rq2 == 3:
        cornival += 2
    elif rq2 == 4:
        grifinoria += 2

    print('')
    #Questão3
    print('Q3) Qual tipo de instrumento mais agrada ao seu ouvido?\n1)O Violino\n2)A Trombeta\n3)O Piano\n4)O Tambor')
    rq3 = int(input('Escolha: '))

    if rq3 == 1:
        sonserina += 4
    elif rq3 == 2:
        lufalufa += 4
    elif rq3 == 3:
        cornival += 4 
    elif rq3 == 4:
        grifinoria += 4

    #Ponturação máxima
    destino = max(grifinoria, sonserina, lufalufa, cornival)
    print(grifinoria, sonserina, lufalufa, cornival)
    if grifinoria == destino:
        print('sua casa é grifinória')
    elif sonserina == destino:
        print('sua casa é sonserina')
    elif cornival == destino:
        print('sua casa é cornival')
    else:
        print('sua casa é lufa-lufa')
    
def EnterPin():
    senha = str(input('Digite a Senha: '))

    while senha != "sakai":
        print('senha incorreta, Digite novamente')
        senha = str(input('Digite a senha: '))
    if senha == "sakai":
        print('Acesso liberado!')

def Adivinhe():
    Adivinhe = 0
    descubra = int(input('qual o número?: '))

    while descubra != 123:
        print('tente de novo!')
        descubra = int(input('qual o número?: '))
        if descubra <= 122:
            print('mais alto')
        elif descubra >= 124:
            print('mais baixo')
        elif descubra == 123:
            print('Achou o número!')

def AdivinheLimitado():
    adivinhe = 0
    tentativas = 0
    numero = random.randint(1, 100)

    while (adivinhe != numero and tentativas != numero):
        adivinhe = int(input('adivinhe o número: '))
        tentativas += 1
        if tentativas == 11:
            print('acabou as tentativas')
            break
        elif adivinhe > numero:
            print('mais baixo')
        elif adivinhe < numero:
            print('mais alto')
        elif adivinhe == numero:
            print('acertou!')

def Detenção():
    for aluno in range(100):
        print('não usar snapchat em sala', aluno)

def Concatenar():
    #Concatenação de String
    for i in range(5):
        print('a quadrado de: ' + str(i) + ' is ' + str(i*i))

def Interpolação():
    #Interpolar String
    for i in range(5):
        print(f'O quadrado de {i} é {i*i}')

def GarrafasDCerveja():
    for ngarrafa in range(99, 0, -1):
        print(f'{ngarrafa} garrafas de cerveja na parede\n{ngarrafa} Garrafas de cerveja\nPegue uma, passe a diante')

def FizzBuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')  
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)




#Run
Adivinhe()


# Avaliações Práticas
#AV1
def Avaliacao_Pratica_1A():
#A) Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
    raio = float(input('Digite o raio R : '))
    volume = (4/3) * 3.14 * (raio**2)

    print(f"O volume da efera de raio R {raio} é igual à: {volume:.2f}")

def Avaliacao_Pratica_1B():
#B) Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles.
    def calcular_distancia(x1, y1, x2, y2):
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia

    x1 = float(input("Digite a coordenada x1 de P: "))
    y1 = float(input("Digite a coordenada y1 de P: "))
    x2 = float(input("Digite a coordenada x2 de Q: "))
    y2 = float(input("Digite a coordenada y2 de Q: "))

    distancia = calcular_distancia(x1, y1, x2, y2)

    print(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é {distancia:.2f}")

def Avaliacao_Pratica_1C(): 
# C) Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário.
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    if valor1 < valor2:
        print(f"A ordem crescente dos valores é: {valor1}, {valor2}")
    elif valor1 > valor2:
        print(f"A ordem crescente dos valores é: {valor2}, {valor1}")
    else:
        print("Os valores são iguais.")

def Avaliacao_Pratica_1D():
#D) Construa o programa que calcule o peso ideal de uma pessoa.
# Utilize as seguintes fórmulas:
#- Se homem, o peso ideal é calculado assim: (72,7 . altura) - 58;
#- Se mulher, o peso ideal é calculado assim: (62,1 . altura) - 44,7.
#Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar).

    sexo = input("Digite o sexo (M para homem, F para mulher): ")
    altura = float(input("Digite a altura em metros: "))

    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido.")
        return

    print(f"O peso ideal para uma pessoa do sexo {sexo} com altura {altura} é {peso_ideal:.2f} kg")

#AV2
def Avaliacao_Pratica_2A():
    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))
    valor3 = float(input("Insira o terceiro valor: "))
    valormax = max(valor1, valor2, valor3)
    print("O maior valor é:", valormax)

def Avaliacao_Pratica_2B():
    valor1 = float(input("Insira o primeiro valor: "))
    valor2 = float(input("Insira o segundo valor: "))
    valor3 = float(input("Insira o terceiro valor: "))

    if valor1 >= valor2 and valor1 >= valor3:
        valormax = valor1
    elif valor2 >= valor1 and valor2 >= valor3:
        valormax = valor2
    else:
        valormax = valor3
    print("O maior valor é:", valormax)

def Avaliacao_Pratica_2C():
    print('''
░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░█▀▄░█▀█░█▀▄░█▀█
░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░█░█░█░█░█▀▄░█▀█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀░▀
''')
    print('Menu:\n[1]Somar\n[2]Subtrair\n[3]Multiplicar\n[4]Dividir\n[5]Sair')
    escolha = int(input('Escolha: '))

    if escolha == 1:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 + n2)
    elif escolha == 2:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 - n2)
    elif escolha == 3:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 * n2)
    elif escolha == 4:
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
        print('Resultado:', n1 / n2)
    elif escolha == 5:
        print('bye bye')