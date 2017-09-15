idade = []
altura = []
for i in range (5):
	x = int(input("Idade {0}: " .format(i+1)))
	y = int(input("Altura {0}: " .format(i+1)))
	idade.append(x)
	altura.append(y)

print(idade)
print(altura)
idade.reverse()
altura.reverse()
print(idade)
print(altura)