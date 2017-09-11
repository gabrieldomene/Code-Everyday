n = int(input("Digite o número para saber sua tabuada: "))
tabuada = 0
for i in range(1,11):
	tabuada = n*i
	print("{1} x {0} = {2}". format(i, n, tabuada))