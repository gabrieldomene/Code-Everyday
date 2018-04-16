class User():
	def __init__ (self, first_name, last_name, nickname, password):
		self.first_name = first_name
		self.last_name = last_name
		self.nickname = nickname
		self.password = password
		self.login_attempts = 0

	def describe_user(self):
		print("{} is the nickname of {}, {}." .format(self.nickname, self.last_name.title(), self.first_name.title()))

	def greet_user(self):
		print("Hello {}, welcome your new pass is: {}" .format(self.nickname, self.password))

	def increment_login_attemps(self):
		self.login_attempts += 1

	def reset_login_attemps(self):
		self.login_attempts = 0

user1 = User("gabriel", "domene", "guina157", "z3usg0d")

user1.describe_user()
user1.increment_login_attemps() #incrementa 1
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
print("{} tried to login {} times" .format(user1.nickname, user1.login_attempts))
user1.reset_login_attemps() #reseta para 0
print("{} tried to login {} times" .format(user1.nickname, user1.login_attempts))

