from django.shortcuts import render
from django.http import HttpResponse
from .models import TVShow
from .forms import EnterTVShowForm

def index(request):
	numTVShows = TVShow.objects.all().count()
	tvList = TVShow.objects.order_by('title')
	print(tvList[0].title)
	context = {'numTVShows': numTVShows, 'tvList': tvList}
	return render(request, 'index.html', context)

def enter_tvshow(request):
	show = TVShow()
	if request.method == "POST":
		form = EnterTVShowForm(request.POST)
		if form.is_valid():
			show.title = request.POST.get("title")
			show.watchedSeasons = request.POST.get("watchedSeasons")
			if request.POST.get("inProgress") == 'on':
				show.inProgress = True
			else:
				show.inProgress = False
			show.seasons = request.POST.get("seasons")
			show.save()
			return HttpResponse("got it")
		print("ERRORS: ", form.errors)
	form = EnterTVShowForm()
	return render(request, 'enter_tvshow.html', {'form': form})