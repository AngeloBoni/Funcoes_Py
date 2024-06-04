#Introdução a funções, parâmetros, retorno

def calcula_soma(min, max, inc):
    soma = 0

    for i in range(min, max, inc):
        print(f"{i} + {soma} = {i + soma}" )
        soma += i
        
    return soma

###Funções recursivas -> Estrutura de dados

x = int(input("Digite o valor: "))
y = int(input("Digite o valor: "))
z = int(input("Digite o valor: "))

s = calcula_soma(x, y, z)

print(s)