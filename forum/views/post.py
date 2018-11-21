import json
from django.http import HttpResponse, JsonResponse
from forum.controllers import Post as PostController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get(request):
	if 'username' not in request.session.keys():
		return HttpResponse("Unauthenticated request!", status=401)
	if request.method!='GET':
		return HttpResponse("Check request method!", status=400)
	params = request.GET
	postID = params['id']
	result, response=PostController.get(postID)
	if result==True:
		return JsonResponse(json.dumps(response, verify=False), status=200)
	else:
		return HttpResponse("Invalid id!", status=400)