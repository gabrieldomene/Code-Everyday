info_person_1 = {"nome" : "Gabriel", "sobrenome" : "Domene", "idade" : 21, "cidade" : "Londrina"}
info_person_2 = {"nome" : "Matheus", "sobrenome" : "Francisco", "idade" : 23, "cidade" : "Jales"}
info_person_3 = {"nome" : "Tulio", "sobrenome" : "Moehlecke", "idade" : 21, "cidade" : "Novo Hamburgo"}

peoples = [info_person_1, info_person_2, info_person_3]

for people in peoples:
	for nome, sobrenome, idade, cidade in people:
		print(nome, sobrenome, idade, cidade)

