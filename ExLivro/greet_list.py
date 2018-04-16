def greet_users(names):
	for name in names:
		msg = ("Hello, {}!" .format(name.title()))
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)