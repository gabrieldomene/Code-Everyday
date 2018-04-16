class Restaurant():
	def __init__ (self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("{} especializado em: {}." .format(self.restaurant_name.title(), self.cuisine_type))

	def open_restaurant(self):
		print("{} is open!" .format(self.restaurant_name.title()))
