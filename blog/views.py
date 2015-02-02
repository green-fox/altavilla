from django.shortcuts import render
from blog.models import Article, Song, Carousel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index(request):	
	carousel_pic = Carousel.objects.order_by('picture')
        song_list =  Song.objects.order_by('song_title')
	article_list= Article.objects.order_by('-creation_date')
        context = {'article_list': article_list, 'song_list': song_list, 'carousel_pic': carousel_pic}
	return render(request, 'blog/index.html', context)



