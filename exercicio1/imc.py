# Escreva um programa que leia peso e altura, calcule o IMC 
#( peso / altura**2 ) e classifique em Abaixo do peso,
#  Peso normal, Sobrepeso ou Obesidade.#
peso: float = float(input("Digite seu peso "))
altura: float = float(input("Digite sua altura "))
resultado = peso / altura**2 
if resultado <= 18.5:
    print("Você está abaixo do peso ")
elif resultado > 18.5 and resultado <=24.9:
    print("Você está no peso normal ")
elif resultado >24.9 and resultado <=29.9:
    print("Você está com sobre peso ")
else :
    print("você está com obesidade ")

