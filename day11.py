saltos = []
media = 0
while(True):
	name = input("Nome do atleta: ")
	if(name == ""):
		break
	else:	
		for i in range(5):
			nota = int(input("Nota {0}: " .format(i+1)))
			saltos.append(nota)
		x = sum(saltos)/5
	print("Média {0} = {1} pontos.".format(name, x))



