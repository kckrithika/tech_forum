from forum.models.User import User as UserModel
def register(username, password):
	if(not(UserModel.objects.filter(pk=username).exists())):
		user = UserModel(_username = username, _password = password)
		try:
			user.save()
		except:
			return 2
		return 1
	else:
		return 0

def login(username, password):
	if UserModel.objects.filter(pk=username, _password=password).exists():
		return True
	return False