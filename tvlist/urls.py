from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('enter_tvshow.html', views.enter_tvshow, name='enter_tvshow')
]
