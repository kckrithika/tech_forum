from django.http import HttpResponse
from forum.controllers import Answer as AnswerController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
	params = request.POST #request.body
	if (not("username" in request.session.keys())):
		return HttpResponse("Unauthenticated user", status = 401)

	author = request.session['username']
	answer = params['answer']
	question = params['question']

	success, message = AnswerController.add(answer, question, author)
	if (success == 0):
		return HttpResponse("Answer added successfully", status=201)
	elif(success == 1):
		return HttpResponse(message, status = 400) # question/asker id is invalid.
	else:
		return HttpResponse("Couldn't serve request, try again later!", status = 500) 