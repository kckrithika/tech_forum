import json
from django.http import HttpResponse, JsonResponse
from forum.controllers import Topic as TopicController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
	params = request.POST
	topic = params['topic']
	if 'parent' in params.keys():
		parent = params['parent']
	else:
		print("Parent not found. Making it none\n")
		parent = None
	result = TopicController.add(topic, parent)
	if result==True:
		return HttpResponse("Topic added", status=201)
	return HttpResponse("Couldnt create new topic, please try again later", status = 500)

@csrf_exempt
def topics(request):
	params = request.GET
	return JsonResponse(json.dumps(TopicController.getAll()), safe=False)
