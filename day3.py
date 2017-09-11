n = int(input("Digite quantos números será inserido: "))
x = []
for i in range(1,n+1):
	datain = int(input())
	x.append(datain)
x.sort()
x.reverse()
print(x)
