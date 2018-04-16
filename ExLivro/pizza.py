def make_pizza(size, *toppings):
	print("\nMaking a {}-inch size pizza with the following toppings: ".format(size))
	for topping in toppings:
		print("- {}." .format(topping.title()))

