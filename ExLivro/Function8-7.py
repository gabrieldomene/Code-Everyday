def make_album(artist_name, album_title):
	album = {"artist" : artist_name, "title" : album_title}
	return album

album1 = make_album("angra", "brasil")
album2 = make_album("metallica", "stormtrooper")
album3 = make_album("3030", "na praia")

print(album1)
print(album2)
print(album3)
