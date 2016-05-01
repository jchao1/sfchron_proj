from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listings/$', views.listings_view, name='listings'),
	url(r'^property/(?P<id>\d{1,10})/$', views.property_view, name='property'),
]
