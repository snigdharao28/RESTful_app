from werkzeug.security import safe_str_cmp
from user import User


#########################
#	replaced by sqlite code in user.py and modifications in line 41 and 47 of present code
# users = [
# 	User(1,'maia','chicklet')
# ]

# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


# users = [
# 	{
# 		'id': 1,
# 		'username': 'maia',
# 		'password': 'chicklet'
# 	}
# ]
#########################

# username_mapping = {
# 	'maia': {
# 		'id': 1,
# 		'username': 'maia',
# 		'password': 'chicklet'
# 	}
# }

# userid_mapping[1]

# userid_mapping = {
# 	1: {
# 		'username':'maia',
# 		'password':'chicklet'
# 	}
# }

def authenticate(username, password):
	user = User.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']
	return User.find_by_id(user_id)

 