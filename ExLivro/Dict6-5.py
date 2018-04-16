#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#•	 Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#•	 Use a loop to print the name of each river included in the dictionary.
#•	 Use a loop to print the name of each country included in the dictionary.

rios = {"Nile" : "Egypt", "São Francisco" : "Brasil", "Rio amarelo" : "China", "Cambézinho" : "Londrina", "Tuai Peig" : "Japão", "Araranguá" : "Brasil"}
print("Rios: ")
for rio in sorted(rios.keys()):
	print(rio)
print("\nLugares: ")
for pais in set(rios.values()):
	print(pais)
print("\nSentença: ")
for rio, pais in rios.items():
	print("The {} runs through {}." .format(rio, pais))