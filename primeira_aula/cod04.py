#Aula 05/08/2026#
nome = str(input("Digite seu nome:"))

peso = float(input("Digite seu peso:"))

altura = float(input("Digite sua altura "))

imc : float = peso / (altura * altura)

print("Bem vindo!", nome, "Seu peso é:", peso, "Sua altura é :", altura, "Seu IMC é", imc)
