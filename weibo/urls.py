from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showWeibo, name='showWeibo'),
    url(r'sentiment',views.showWeiboSentiment, name='showWeiboSentiment'),
    url(r'original',views.showWeiboOriginal, name='showWeiboOriginal'),
]