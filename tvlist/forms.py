from django import forms
from django.db import models

class EnterTVShowForm(forms.Form):
	title = forms.CharField(label="Show title")
	seasons = forms.IntegerField(label="Total seasons", min_value=1)
	watchedSeasons = forms.IntegerField(label="Watched seasons", min_value=0)
	inProgress = forms.BooleanField(label="Currently watching", required=False)