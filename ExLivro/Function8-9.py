def show_magicians(list_magicians):
	for magician in list_magicians:
		print("{} is a magician!!" .format(magician.title()))

lista = ["houdini", "mister m", "gabriel"]
show_magicians(lista)