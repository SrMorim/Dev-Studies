print(''' 
░█▀▀░█▀█░█░░░█▀▀░█░█░█░░░█▀█░█▀▄░█▀█░█▀▄░█▀█
░█░░░█▀█░█░░░█░░░█░█░█░░░█▀█░█░█░█░█░█▀▄░█▀█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀░▀
''')
print('menu:\n1)soma\n2)subtração\n3)multiplicação\n4)divisão')

escolha = int(input('escolha uma opção: '))
if escolha == 1:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: ')) 
    soma = n1+n2
    print('O resultado da sua soma é: ', soma)
elif escolha == 2:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: ')) 
    subtrair = n1-n2
    print('O resultado da sua subtração é: ', subtrair)
elif escolha == 3:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: ')) 
    multiplicar = n1*n2
    print('O resultado da sua multiplicação é: ', multiplicar)
elif escolha == 4:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: ')) 
    dividir = n1/n2
    print('O resultado da sua divisão é: ', dividir)
else:
    print('escolha uma das opçõe')
