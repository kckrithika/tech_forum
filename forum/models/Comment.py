from django.db import models
from forum.models.Question import Question
from forum.models.User import User
from forum.models.Answer import Answer

class Comment(models.Model):
	_id = models.AutoField(primary_key=True)
	_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
	_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
	_comment = models.TextField()
	_author = models.ForeignKey(User, on_delete=None)
	_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "Comments"