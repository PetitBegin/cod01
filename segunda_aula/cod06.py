#Distância,  valor do combustível, quantos litros gastou, valor total da viagem#
distancia = float(input("Digite a distância percorrida:"))
valor_do_litro_do_combustivel = float(input("Digite o valor do litro do combustível:"))
litros_gastos = float(input("Digite quantos litros foram colocados no veículo:"))
custo_total: float = valor_do_litro_do_combustivel * litros_gastos

print("Sua disância foi:", distancia, "O valor total da sua viagem é:", custo_total)