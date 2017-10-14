from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class DataSet(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	description = models.TextField()
	file = models.FileField()
	publishing_date = models.DateField(default=datetime.now(), blank=True)
	votes = models.IntegerField(default = 0, blank = True)

	def upVote(self):
		self.votes += 1

	def downVote(self):
		self.votes -= 1