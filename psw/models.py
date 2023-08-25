


# Create your models here.
from django.db import models

class User(models.Model):
	title = models.CharField(max_length=255)
	password = models.CharField(max_length=10)
	


	def __str__(self) -> str:
		return self.title


