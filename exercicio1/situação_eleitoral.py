#Escreva um programa que leia a idade de uma pessoa e informe sua
#  situação eleitoral: menor de 16(não vota), 16 ou 17 
# (voto facultativo), 18 a 70 (voto obrigatório), acima de 70
#  (voto facultativo).#
idade: int = int(input("Digite sua idade" )) #16
if idade <16: # NÃO ENTRA
    print("Você não vota ")
elif idade >=16 and idade <=17:
    print("Seu voto é facultativo ")
elif idade >17 and idade <= 70: 
    print("o seu voto é obrigatorio")
elif idade >70 :
    print("Seu voto é facultativo ")

    
