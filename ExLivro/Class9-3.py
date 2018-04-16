class User():
	def __init__ (self, first_name, last_name, nickname, password):
		self.first_name = first_name
		self.last_name = last_name
		self.nickname = nickname
		self.password = password

	def describe_user(self):
		print("{} is the nickname of {}, {}." .format(self.nickname, self.last_name.title(), self.first_name.title()))

	def greet_user(self):
		print("Hello {}, welcome your new pass is: {}" .format(self.nickname, self.password))

user1 = User("gabriel", "domene", "guina157", "z3usg0d")
user2 = User("rafael", "araujo", "rafarujo", "f3t0litcho")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
