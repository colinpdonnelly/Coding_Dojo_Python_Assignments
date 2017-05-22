from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^suprise$', views.suprise),
    url(r'^my_list$', views.my_list)
]
