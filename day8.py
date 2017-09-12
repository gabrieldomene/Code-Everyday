cod = []
altura = []
massa = []
maior, menor, maiorpeso, menorpeso = 0, 0, 0, 0

while(True):
	v1 = int(input("Digite cod cliente: "))
	if(v1 == 0):
		break;
	else:
		cod.append(v1)
		v2 = int(input("Digite a massa: "))
		massa.append(v2)
		v3 = int(input("Digite a altura: "))
		altura.append(v3)

maior = altura[0]
menor = altura [0]
maiorpeso = massa [0]
menorpeso = massa [0]
mediamassa = 0
mediaaltura = 0
for i in range(len(cod)):
	if(massa[i] >= maiorpeso):
		maiorpeso = massa[i]
		codpesomais = i+1
	elif(massa[i] <= menorpeso):
		menorpeso = massa[i]
		codpesomenos = i+1
	if(altura[i] >= maior):
		maior = altura[i]
		codalturamais = i+1
	elif(altura[i] <= menor):
		menor = altura[i]
		codalturamenos = i+1
	mediamassa = mediamassa + massa[i]
	mediaaltura = mediaaltura + altura[i]

mediaaltura = mediaaltura/len(cod)
mediamassa = mediamassa/len(cod)

print("Cod: ", cod)
print("Massa: ", massa)
print("Altura: ", altura)
print("Maior peso: ", maiorpeso)
print("Menor peso: ", menorpeso)
print("Maior altura: ",maior)
print("Menor altura: ", menor)
print("Cod peso+: ",codpesomais)
print("Cod peso-: ",codpesomenos)
print("Cod altura+: ",codalturamais)
print("Cod altura-: ",codalturamenos)
print("Media massa: ", mediamassa)
print("Media altura: ", mediaaltura)
