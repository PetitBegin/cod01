#Escreva um programa que leia dois números em variáveis a e b e,
#  usando uma variável auxiliar,troque os valores entre elas,
#  imprimindo o resultado antes e depois da troca.#
a: float = float(input("Digite o primeiro valor:")) 
b: float = float(input("Digite o segundo valor:"))

print(f"Seu valor de a é,{a}, \nSeu valor de b é, {b}")

auxiliar: float = float (a+b) 

a = auxiliar - a 
b = auxiliar - b 

print("O valor trocado de a é :",a,"\nPorque virou o valor de B" ,"\nSeu valor de b é :",b, "\nPorque virou o valor de A")