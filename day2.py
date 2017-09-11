a = int(input("Digite em m² da área a ser pintada: "))
litros = a/3
qtd = 0
while(litros/18 >= 1):
	qtd = qtd + 1
	litros = litros - 18
if(litros > 0):
	qtd = qtd+1
total = qtd * 80
print("Será necessário {0} latas de tintas, no total de R${1} " .format(qtd, total))