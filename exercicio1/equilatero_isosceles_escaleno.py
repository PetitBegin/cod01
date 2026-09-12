#Escreva um programa que leia os três lados de um triângulo e classifique-o
#  em equilátero (todos oslados iguais), isósceles (dois lados iguais)
#  ou escaleno (todos diferentes).#
lado1: int =int(input("Digite o primeiro lado do triângulo "))
lado2: int =int(input("Digite o segundo lado do triângulo "))
lado3: int =int(input("Digite o terceiro lado do triângulo "))
if lado1 == lado2 and lado1 == lado3:
    print("Seu triângulo é equilátero ")
elif lado1 ==lado2 or lado1 == lado3 or lado2 == lado3:
    print("Seu triângulo é isósceles ")
else:
     print("Seu triângulo é escaleno ")
