import sys
d, m, a = map(int, input().split("/"))
if(d <= 31 and d >=1 and m<=12 and m>=1 and a >= 0):
	print("Data válida")
else:
	print("Data inválida!")