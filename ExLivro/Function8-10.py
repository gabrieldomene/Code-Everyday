def make_great(list_magician):
	for magician in list_magician:
		new = ("The great {}!!" .format(magician.title()))
		magicos.append(new)
		print(new)
	return magicos

def show_magician(list_magician):
	print(list_magician)

lista = ["houdini", "mister m", "gabriel"]
magicos = make_great(lista)
show_magician(lista)
print(magicos)