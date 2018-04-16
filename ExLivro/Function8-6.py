def city_country(city, country):
	info = ("{}, {}" .format(city, country))
	return info

while True:
	print("\nDigite 'quit' para sair a qualquer momento!")
	in_city = input("Digite uma cidade: ")
	if in_city == "quit":
		break
	in_country = input("Digite um país: ")
	if in_country == "quit":
		break
	final = city_country(in_city, in_country)
	print('"{}"' .format(final))