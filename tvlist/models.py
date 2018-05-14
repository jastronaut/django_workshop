from django.db import models

# Create your models here.
class TVShow(models.Model):
	title = models.CharField(max_length=50)
	seasons = models.IntegerField(default=1)
	watchedSeasons = models.IntegerField("Watched seasons", default=0)
	inProgress = models.BooleanField("Currently watching", default=False)