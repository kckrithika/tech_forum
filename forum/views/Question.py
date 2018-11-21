import json
from django.http import HttpResponse, JsonResponse
from forum.controllers import Question as QuestionController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
	if 'username' not in request.session.keys():
		return HttpResponse("Unauthenticated request!", status=401)
	if request.method!='POST':
		return HttpResponse("Check request method!", status=400)
	params = request.POST
	question = params['question']
	asker = request.session['username']
	print(asker)
	topic = params['topic']
	if QuestionController.add(asker, question, topic) == False:
		return HttpResponse("Couldnt add question, Try Again!", status=500)
	else:
		return HttpResponse(status=200)
	

def questions(request):
	if 'username' not in request.session.keys():
		return HttpResponse("Unauthenticated request!", status=401)
	if request.method!='GET':
		return HttpResponse("Check request method!", status=400)
	return JsonResponse(json.dumps(QuestionController.getAll()), safe=False)