from forum.models.Comment import Comment as CommentModel
from forum.models.User import User
from forum.models.Question import Question
def add(type, comment, author, id):
	try:
		author = User.objects.filter(pk=author).get()
		if type == "q":
			question = Question.objects.filter(pk=id).get()
			cm = CommentModel(_comment=comment, _author=author, _question=question, _answer=None)
		elif type == "a":
			answer = Answer.objects.filter(pk=id).get()
			cm = CommentModel(_comment=comment, _author=author, _question=None, _answer=answer)
		else:
			return (1, "Invalid comment type. Comment type can be 'q' or 'a' ")
		cm.save()
		return (0, "Comment added successfully!")
	except Exception as e:
		print(e)
		return (2, "Internal server error")

def getQuestionComments(question):
	result=[]
	records = CommentModel.objects.filter(_question=question).values()
	for record in records:
		for key in record:
			record[key] = str(record[key])
		result.append(record)
	return result

def getAnswerComments(answer):
	result=[]
	records = CommentModel.objects.filter(_answer=answer).values()
	for record in records:
		for key in record:
			record[key] = str(record[key])
		result.append(record)
	return result