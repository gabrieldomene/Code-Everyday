#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.


glossary = {"IF" : "Sentença condicional", "ELSE" : "Parte false do if", "Lista" : "Formato mutável de dados", "Python" : "Linguagem de programação",
	"Dicionários" : "Forma de armazenamento chave:valor", "Variável" : "Armazena dados"}

for chaves, valor in sorted(glossary.items()):
	print("{}, {}." .format(chaves, valor))