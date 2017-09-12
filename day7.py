n = int(input("Número de pessoas: "))
soma = 0
for i in range(n):
	x = int(input("Idade: "))
	soma = soma + x
if((soma/n) >= 0 and (soma/n)<26):
	print("A turma é jovem, com média de {:.2f} anos" .format(soma/n))
elif((soma/n)>=26 and (soma/n)<60):

	print("A turma é adulta, com média de {:.2f} anos" .format(soma/n))
else:
	print("A turma é idosa, com média de {:.2f} anos" .format(soma/n))