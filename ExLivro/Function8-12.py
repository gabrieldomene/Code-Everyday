def create_list_items(*items):
	print("\nItems ordered in the sandwich: ")
	for item in items:
		print("- {}." .format(item.title()))

create_list_items("presunto", "mussarela")
create_list_items("mortadela", "ovo", "bacon", "queijo")