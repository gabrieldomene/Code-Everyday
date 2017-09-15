saltos = []
media = 0
while(True):
	name = input("Nome do atleta: ")	
	saltos = (int, input("Digite os valores das notas: ").split())
	for i in range(5):
		media = int(saltos[i]) + media
	media = media/5
	print(media)


