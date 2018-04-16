def build_profile(first, last, **user_info):
	profile = {}
	profile["first_name"] = first
	profile["last_name"] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
cidade = input("Digite sua cidade: ")
perfil = build_profile(nome, sobrenome, cidade=cidade)
print(perfil)