#Escreva um programa que leia um ano e informe se
#  ele é bissexto (divisível por 4 e, se divisível por 
# 100, também precisa ser divisível por 400).#
bissexto: int = int(input("Digite o ano desejado "))
if bissexto % 4 == 0 and bissexto % 100 != 0 or bissexto % 400 == 0:    
    print("Seu ano é bissexto ")
else:
    print("Seu ano não é bissexto ")

