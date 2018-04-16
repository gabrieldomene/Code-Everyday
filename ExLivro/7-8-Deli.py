sandwich_orders = ["presuntao", "queijo quente", "mortadela", "x-burger"]
finished_sandwiches = []

while sandwich_orders:
	making = sandwich_orders.pop()
	print("I made your {}" .format(making))
	finished_sandwiches.append(making)

print("\nSandwiches made: ")

for sandwich in finished_sandwiches:
	print(sandwich.title())