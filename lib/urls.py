from django.conf.urls import url
from . import views

app_name = 'lib'

urlpatterns = [
   url(r'^$', views.index, name='index'),
]

