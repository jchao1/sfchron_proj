from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listings/$', views.listings_view, name='listings'),
	url(r'^property/(?P<id>\d+)/$', views.property_view, name='property'),
	url(r'^profile/$', views.profile_view, name='profile'),
]
