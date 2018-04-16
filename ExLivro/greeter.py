username = input("Qual seu nome? ")

def greet_user(username):
	print("Hello! {}!" .format(username.title()))

greet_user(username)