from django.db import models
from forum.models.Question import Question
from forum.models.User import User

class Answer(models.Model):
	_id = models.AutoField(primary_key=True)
	_question = models.ForeignKey(Question, on_delete=models.CASCADE)
	_answer = models.TextField()
	_author = models.ForeignKey(User, on_delete=None)
	_time = models.DateTimeField(auto_now_add=True)
	_best = models.BooleanField(default=False)

	class Meta:
		db_table = "Answers"