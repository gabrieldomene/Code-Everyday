def make_album(artist_name, album_title):
	album = {"artist name" : artist_name, "album title" : album_title}
	return album

while True:
	print("\nDigite 'quit' para sair a qualquer momento\n")
	artista = input("Digite um artista: ")
	if artista == "quit":
		break
	album = input("Digite um album: ")
	if album == "quit":
		break
	dic_album = make_album(artista, album)
	print(dic_album)