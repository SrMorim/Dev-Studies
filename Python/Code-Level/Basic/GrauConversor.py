print('Opções:\n1)Celsius > Fahrenheit\n2)Fahrenheit > Celsius')

escolha = int(input('Escolha uma opção: '))
if escolha == 1:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = celsius * 1.8 * 32
    print('A temperatura em Fahrenheit é: ', fahrenheit)
elif escolha == 2:
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print('A temperatura em Celsius é: ', celsius)
else:
    print('Escolha uma das opções')