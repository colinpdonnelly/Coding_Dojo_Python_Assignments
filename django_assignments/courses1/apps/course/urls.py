from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<num>\d+)$', views.destroy),
    url(r'^eliminate/(?P<num>\d+)$', views.eliminate)
    # url(r'^/remove$', views.remove),
    # url(r'^remove/(?P\d+)$', views.remove, name='remove')
]
