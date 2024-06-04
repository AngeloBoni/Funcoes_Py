#Passando funções como parâmetro

def numero(numero):
    soma = 0
    for i in range(numero):
        soma += i
    return soma

def teste(numero):
    print(numero)

x = int(input("Quantos números você deseja somar? "))

teste(numero(x))