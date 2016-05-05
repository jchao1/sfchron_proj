from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listings/$', views.listings_view, name='listings'),
    url(r'^roommates/$', views.roommates_view, name='roommates'),
	url(r'^openhouse/$', views.openhouse_view, name='openhouse'),
	url(r'^profile/$', views.profile_view, name='profile'),
	url(r'^property/(?P<id>\d+)/$', views.property_view, name='property'),
	url(r'^user/(?P<id>\d+)/$', views.user_view, name='user'),
]
