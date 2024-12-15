#Libs
import random

#Lista
frases = [
    "A sorte favorece os audaciosos.",
    "Grandes oportunidades virão em breve.",
    "A persistência é o caminho do sucesso.",
    "A felicidade está ao seu alcance, apenas estenda a mão.",
    "Confie nos seus instintos, eles te guiarão bem.",
    "Mudanças positivas estão no horizonte.",
    "O amor está mais perto do que você imagina.",
    "Seu trabalho árduo logo será recompensado.",
    "A paciência é a chave para tudo de bom.",
    "Novas amizades trarão grandes alegrias."
]

#Função
escolha = str(input('Abrir biscoito da sorte? (y/n)\n>>> '))

if escolha == "y":
    print('sua frase é:', random.choice(frases))
else:
    print('Bye Bye!')