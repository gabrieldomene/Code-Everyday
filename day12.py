import random 
x = []
c = []
for i in range(100):
	n = random.randint(1,6)
	x.append(n)
for i in range(1,7):
	count = x.count(i)
	c.append(count)

print('''Um dado é jogado 100x para cima, contador de ocorrência:
{0} vezes o número 1
{1} vezes o número 2
{2} vezes o número 3
{3} vezes o número 4
{4} vezes o número 5
{5} vezes o número 6''' .format(c[0],c[1],c[2],c[3],c[4],c[5], ))
	
