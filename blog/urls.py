from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from blog import views

#urlpatterns = patterns('',
#    url(r'^$', views.index, name='index')
#)

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^test/$', views.test, name='test'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#	url(r'^' + settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

#urlpatterns += patterns('',
#       	(r'^' + settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

