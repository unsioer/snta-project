from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showTwitter, name='showTwitter'),
	#url(r'sentiment',views.showTwitterSentiment, name='showTwitterSentiment'),
	url(r'original',views.showTwitterOriginal, name='showTwitterOriginal'),
]