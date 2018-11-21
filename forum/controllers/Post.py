from forum.controllers import Question, Comment, Answer

def get(id):
	quest = Question.get(id)
	comm = Comment.getQuestionComments(id)
	ans = Answer.get(id)
	