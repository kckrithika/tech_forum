from django.http import HttpResponse
from forum.controllers import Comment as CommentController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
	if('username' not in request.session.keys()):
		return HttpResponse("Unauthenticated user", status=401)
	params = request.POST #request.body
	keys = params.keys()
	if(('comment' not in keys) or ('type' not in keys) or ('ref' not in keys)):
		return HttpResponse("Invalid request data", status=400)
	
	comment = params['comment']
	author = request.session['username']
	type = params['type']
	reference = params['ref']
	result, message = CommentController.add(type, comment, author, reference)
	if result==0:
		return HttpResponse("Added successfully", status=201)
	elif result==1:
		return HttpResponse(message, status=400)
	else:
		return HttpResponse(message, status=500)
