from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	path('polls/psychometry/',views.post_new,name="add_new_polls_qresult"),
    url(r'^$', views.index, name='index'),
]