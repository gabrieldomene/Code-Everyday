#6-6. Polling: Use the code in favorite_languages.py (page 104).
#108     Chapter 6
#•	 Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#•	 Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll

favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
}

should_take_poll = ["gabriel", "jen", "sarah", "matheus", "edward", "ale", "luan"]

for name in should_take_poll:
	if name in favorite_languages:
		print("{}, thanks for responding." .format(name.title()))
	else:
		print("{}, you'd be welcome to take the poll." .format(name.title()))