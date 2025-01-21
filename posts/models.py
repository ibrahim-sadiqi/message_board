from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name='Title', null=True)
	text = models.TextField(verbose_name='Text')

	def __str__(self):
		return self.title

