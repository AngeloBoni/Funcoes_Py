#Parâmetros default
def ParDef(valor, percentual = 10):
    return valor * percentual/100

x = float(input("Qual o valor da compra?: "))
#y = float(input("Qual o percentual da gorjeta?: "))

print(f"O valor da gojeta é: {ParDef(x)}")