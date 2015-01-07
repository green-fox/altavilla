from django.shortcuts import render
from blog.models import Article, Concert


# Create your views here.
def index(request):	
	article_list= Article.objects.order_by('-creation_date')
	concert_list= Concert.objects.order_by('paf')
	context = {'article_list': article_list, 'concert_list' : concert_list }
	return render(request, 'blog/index.html', context)





