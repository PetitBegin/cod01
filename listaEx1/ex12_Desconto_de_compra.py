#Escreva um programa que leia o valor de uma compra e aplique
#  desconto por faixa: até R$100 sem desconto, de R$100 a R$500 
# com 5%,acima de R$500 com 10%. Imprima o valor final.#
valor_da_compra: float = float(input("Digite o valor da sua compra "))
if valor_da_compra <=100:
    print("Você não possui desconto ")

elif valor_da_compra >100 and valor_da_compra <= 500:
    print(valor_da_compra-(valor_da_compra*(5/100))) 

else:
    print(valor_da_compra-(valor_da_compra*(10/100)))

        