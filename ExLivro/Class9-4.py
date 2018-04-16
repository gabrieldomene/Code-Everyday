class Restaurant():
	def __init__ (self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("{} especializado em: {}." .format(self.restaurant_name.title(), self.cuisine_type))

	def open_restaurant(self):
		print("{} is open!" .format(self.restaurant_name.title()))

	def update_number_served(self, number):
		if number >= self.number_served:
			self.number_served = number
		else:
			print("Impossível diminuir clientes servidos!")

	def set_number_served(self, cliente):
		self.number_served += cliente

	def read_served(self):
		print("This restaurant has served {} meals today" .format(self.number_served))

restaurante1 = Restaurant("Dominos", "pizzaria")
restaurante1.describe_restaurant()
restaurante1.open_restaurant()
restaurante1.read_served()
restaurante1.update_number_served(13)
restaurante1.update_number_served(1)
restaurante1.read_served()

