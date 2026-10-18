#8. Escreva um programa que leia um número
#  e informe se ele é positivo, negativo ou zero.#
numero: float = float(input("Digite um número"))
if numero > 0 :
    print("Seu número é positivo ")
elif numero < 0:
    print("Seu numero é negativo ")
else :
    print("Seu número é zero ")