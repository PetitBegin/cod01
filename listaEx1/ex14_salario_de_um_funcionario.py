#Escreva um programa que leia o salário de um funcionário e aplique reajuste por faixa: até R$1.500 → 10%; de R$1.500 a R$3.000 → 7%; acima de R$3.000 → 5%. Imprima o novo salário.
sal_de_funcionario: float = float (input('Digite o valor do seu salário:'))
print("O valor do salário informado sem reajuste é:",sal_de_funcionario)
if sal_de_funcionario <= 1500:
    print("Seu salário  com reajuste é:",sal_de_funcionario+(sal_de_funcionario*(10/100)))

elif sal_de_funcionario > 1500 and sal_de_funcionario <= 3000:
    print("Seu salário com reajuste é:",sal_de_funcionario+(sal_de_funcionario*(7/100)))

elif sal_de_funcionario > 3000:
    print("Seu salário com reajuste é:",sal_de_funcionario + (sal_de_funcionario*(5/100)))