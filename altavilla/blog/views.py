from django.shortcuts import render
from blog.models import Article


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index(request):	
	article_list= Article.objects.order_by('-creation_date')
	context = {'article_list': article_list}
	return render(request, 'blog/index.html', context)


# index+ paginator
def listing(request):
    artcile_list = Article.objects.order_by('-creation_date')
    paginator = Paginator(article_list, 25) # Show 25 contacts per page

    page = request.GET.get(page)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        arcticles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articless = paginator.page(paginator.num_pages)

    return render_to_response('blog/index.html', {"articles": articles})

