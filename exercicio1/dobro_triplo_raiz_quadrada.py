#6. Escreva um programa que leia um número e imprima seu dobro, seu triplo e sua raiz quadrada.#
numero:float = float(input("Digite um número: "))
dobro: float = numero * 2
print(f"O dobro do número informado é: {dobro}")
triplo: float = numero + dobro 
print(f"O triplo do número informado é: {triplo}")
raiz: float = numero ** (0.5)

print(f"Sua raiz quadrada é:  {raiz}")

