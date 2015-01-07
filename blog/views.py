from django.shortcuts import render
from blog.models import Article, Concert


# Create your views here.
def index(request):	
	article_list= Article.objects.order_by('-creation_date')
	context = {'article_list': article_list}
	return render(request, 'blog/index.html', context)



