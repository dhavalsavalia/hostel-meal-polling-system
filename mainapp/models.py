from django.db import models
from django.contrib.auth.models import User

QUESTION_CHOICES = (
		("vada_paw", "Vada Paw"),
		("paw_bhaji", "Paw Bhaji"),
		("ghughra", "Ghughra"),
		("pani_puri", "Pani Puri"),
		("dal_pakwan", "Dal Pakwan"),
		("fruit_salad", "Fruit Salad"),
		("sandwhich", "Sandwhich"),
		("bhajiya", "Bhajiya"),
		("punjabi", "Punjabi"),
		("pizza", "Pizza"),
		("dabeli", "Dabeli"),
		("manchurian", "Manchurian"),
	)


class Profile(models.Model):
	user = models.ForeignKey(User)
	has_voted = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user)

class Choice(models.Model):
	users   = models.ManyToManyField(User)
	choices = models.CharField(max_length=256, choices=QUESTION_CHOICES, unique=True)
	vote    = models.IntegerField(default=0)

	def __str__(self):
		return self.choices + " " + "-" + " " + str(self.vote)
