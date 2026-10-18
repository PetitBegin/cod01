#Escreva um programa que leia um número inteiro
#  e informe se ele é par ou ímpar,
#  usando o operador %.#

numero: int = int(input("Digite o número "))
if numero % 2 == 0:
    print("Este número é par ")
elif numero % 2 == 1:
    print("Este número é ímpar ")

