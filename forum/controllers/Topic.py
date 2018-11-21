from forum.models.Topic import Topic as TopicModel
def add(topic, parent):
	print("Controller")
	try:
		if(parent!=None):
			parent = TopicModel.objects.filter(pk=parent).get()
		tm = TopicModel(_topic = topic, _parent=parent)
		tm.save()
	except Exception as e:
		print(e)
		return False
	return True

def get(id):
	record = TopicModel.objects.filter(pk=id).values()[0]
	print(record)
	return record['_topic']

def getAll():
	result=[]
	records = TopicModel.objects.all().values()
	for record in records:
		for key in record:
			record[key] = str(record[key])
		result.append(record)
	return result