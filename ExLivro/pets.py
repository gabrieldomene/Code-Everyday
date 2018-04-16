def describe_pet(animal_type, pet_name):
	print("\nI have a {}." .format(animal_type))
	print("My {}'s name is {}." .format(animal_type, pet_name.title()))

a = input("Qual tipo de animal? ")
b = input("Nome dele? ")
describe_pet(a, b)
describe_pet("hamster", "willie")
describe_pet("harry", "hamster")