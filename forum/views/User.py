from django.http import HttpResponse
from forum.controllers import User as UserController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
	params = request.POST #request.body
	username = params['username']
	password = params['password']
	result = UserController.register(username, password)
	if result==1:
		return HttpResponse("User Created", status=201)
	elif result==0:
		return HttpResponse("User already exists", status=409)
	else:
		return HttpResponse("Couldnt process request unexpectedly, try again", status=500)

@csrf_exempt
def login(request):
	params = request.POST
	username = params['username']
	password = params['password']
	if UserController.login(username, password) == True:
		request.session['username']=username
		return HttpResponse("Login successful", status=200)
	else:
		return HttpResponse("Invalid credentials", status=401)

@csrf_exempt
def logout(request):
	del request.session['username']
	return HttpResponse("Logged out successfully", status=204)
