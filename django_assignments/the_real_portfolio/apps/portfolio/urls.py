from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='portfolio'),
    url(r'^testimonials/$', views.testimonials, name='testimonials'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^about/$', views.about, name='about')
]
