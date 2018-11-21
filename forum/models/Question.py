from django.db import models
from forum.models.User import User
from forum.models.Topic import Topic

class Question(models.Model):
	_id = models.AutoField(primary_key=True)
	_question = models.TextField()
	_asker = models.ForeignKey(User, on_delete=models.CASCADE)
	_time = models.DateTimeField(auto_now_add=True)
	_answerer = models.ForeignKey(User, on_delete=None, default=None, null=True)
	_topic = models.ForeignKey(Topic, on_delete=None)
	_closed = models.BooleanField(default=False)

	class Meta:
		db_table = "Questions"