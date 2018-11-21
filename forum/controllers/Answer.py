from forum.models.Answer import Answer as AnswerModel
from forum.models.User import User
from forum.models.Question import Question

def add(answer, question, author):
	try:
		questionQuery = Question.objects.filter(pk=question)
		if (not(questionQuery.exists())):
			return (1, "Question does not exist")
		authorQuery = User.objects.filter(pk=author)
		author = authorQuery.get()		
		question = questionQuery.get()
		answerduplicate = AnswerModel.objects.filter(_author=author, _question=question).exists()
		if answerduplicate == True:
			return (1, "Current user already contributed an answer to this question!")
		am = AnswerModel(_question = question, _author = author, _answer = answer)
		am.save()
	except Exception as e:
		print(e)
		return (2, "Internal server error")
	return (0, "Answer added")

def get(question):
	result=[]
	records = CommentModel.objects.filter(_question=question).values()
	for record in records:
		for key in record:
			record[key] = str(record[key])
		result.append(record)
	return result