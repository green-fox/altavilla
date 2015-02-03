from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from blog import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#	url(r'^' + settings.MEDIA_URL.lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

