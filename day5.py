print('''A - Álcool => 3% de desconto até 20L, acima disso 5% \nB - Gasolina => 4% de desconto até 20L, acima disso 6%''')
tipo = input("Digite o tipo de combustível: ")
tipo.upper()

if( tipo == "A"):
	qtd = int(input("Quantidade de litros desejada: "))
	if(qtd   <= 20 and qtd >= 0):
		total = (qtd*2.5)*0.97
		semdesconto = qtd*2.5
		print("Total sem desconto: R${:.2f}\nTotal com desconto: R${:.2f}" .format(semdesconto, total)) # {:.2f} é minha var de 2 casa decimal, .format(var1, var2) ordem que elas aparecem
	elif(qtd > 20 and qtd >=0):
		total = (qtd*2.5)*0.95
		semdesconto = qtd*2.5
		print("Total sem desconto: R${:.2f}\nTotal com desconto: R${:.2f}" .format(semdesconto, total))
	else:
		print("Impossível litros negativos")
elif( tipo == "B"):
	qtd = int(input("Quantidade de litros desejada: "))
	if(qtd   <= 20 and qtd >= 0):
		total = (qtd*2.5)*0.96
		semdesconto = qtd*2.5
		print("Total sem desconto: R${:.2f}\nTotal com desconto: R${:.2f}" .format(semdesconto, total))
	elif(qtd > 20 and qtd >=0):
		total = (qtd*2.5)*0.94
		semdesconto = qtd*2.5
		print("Total sem desconto: R${:.2f}\nTotal com desconto: R${:.2f}" .format(semdesconto, total))
	else:
		print("Impossível litros negativos")
else:
	print("Tipo inválido")

