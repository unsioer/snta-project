from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showDXY, name='showHubei'),
    url(r'cities',views.showDXYCities, name='showHubeiCities'),
    url(r'class',views.showDXYClass, name='showHubeiPCA'),
]