from django.db import models

class User(models.Model):
	_username = models.CharField(max_length=50, primary_key=True)
	_password = models.CharField(max_length=15)

	class Meta:
		db_table = "Users"