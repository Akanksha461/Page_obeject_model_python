from operator import itemgetter

# we can store test data in this module like users

Merchants = [
	{"name": "valid_user", "email": "testissue@yopmail.com", "password": "12345678"},
	{"name": "invalid_user", "email": "testissue@yopmail.com", "password": "password"},
	{"name": "demo", "email": "infiniarest@yopmail", "password": "password"},
	{"name": "employee", "email": "staff@test.com", "password": "qwert1235"}
]

def get_Merchants(name):

	try:
		return [user for user in Merchants if user["name"] == name][0]
	except:
		print ("\n User %s is not defined, enter a valid user.\n" %name)


employeelist = [
	{"name": "akanksha", 'pin':'9431'},
	{"name": "BHUP", 'pin':'0000'},
    {"name": "Bhup_invalid", 'pin':'3341'}
]

def get_employeelist(name):

	try:
		return [user for user in employeelist if user["name"].lower() == name.lower()][0]
	except:
		print ("\n User %s is not defined, enter a valid user.\n" %name)
