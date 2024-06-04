import time

def menu():
    print("*******************")
    print("1 - Somar")
    print("2- Subtrair")
    print("3 - Dividir")
    print("4 - Multiplicar")
    print("5 - Sair")
    print("*******************")

def soma():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    return a+b

def subtrair():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    return a - b

def multiplicar():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    return a * b

def dividir():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    return a/b


menu()

x = input("Qual operação deseja realizar: ")

while x != "5":

    if x == "1":
        resultado = soma()
        print(f"Resultado da adição = {resultado}")
    elif x == "2":
       resultado =  subtrair()
       print(f"Resultado da subtração = {resultado}")
    elif x == "3":
        resultado = dividir()
        print(f"Resultado da divisão = {resultado}")
    elif x == "4":
        resultado = multiplicar()
        print(f"Resultado da multiplicação = {resultado}")
    else:
        print("O valor inserido foi diferente dos propostos, operação invalida")

    time.sleep(1)
    menu()
    
    x = input("Qual operação deseja realizar: ")

print("********************* Fim do Programa **********************")
