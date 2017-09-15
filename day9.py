print("H = 1 + 1/2 + 1/3 + .... + 1/N")
n = int(input("Insira o número N: "))
h = 0
for i in range(1,n+1):
	h = h+ 1/i
print("Soma dos termos = {:.5f}" .format(h))