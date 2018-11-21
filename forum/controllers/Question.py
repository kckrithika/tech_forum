from django.forms.models import model_to_dict
from forum.models.Question import Question as QuestionModel
from forum.models.User import User
from forum.models.Topic import Topic
from forum.controllers import Topic as TopicController
def add(asker, question, topic):
	try:
		asker = User.objects.filter(pk=asker).get()
		topic = Topic.objects.filter(pk=topic).get()
		qm = QuestionModel(_question=question, _asker=asker, _topic=topic)
		qm.save()
	except Exception as e:
		print(e)
		return False
	return True

def updateAnswerer(qid, answerer):
	noOfRecordsUpdated = QuestionModel.objects.filter(pk=qid).update(_answerer = answerer)
	if noOfRecordsUpdated == 0:
		return False
	return True

def markAsClosed(qid):
	noOfRecordsUpdated = QuestionModel.objects.filter(pk=qid).update(_closed=True)
	if noOfRecordsUpdated == 0:
		return False
	return True

def get(id):
	result=[]
	records = QuestionModel.objects.filter(pk=id).values()
	for record in records:
		print(record)
		for key in record:
			if key == '_topic':
				record[key] = TopicController.get(record[key])
			record[key] = str(record[key])
		result.append(record)
	return result

def getAll():
	result=[]
	records = QuestionModel.objects.all().values()
	for record in records:
		print(record)
		for key in record:
			if key == '_topic':
				record[key] = TopicController.get(record[key])
			record[key] = str(record[key])
		result.append(record)
	return result