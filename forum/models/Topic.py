from django.db import models

class Topic(models.Model):
	_id = models.AutoField(primary_key=True)
	_topic = models.CharField(max_length=50)
	_parent = models.ForeignKey('self', on_delete=models.CASCADE, default = None, null=True)

	class Meta:
		db_table = "Topics"