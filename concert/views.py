#===========
#==Imports== 
#============


from django.shortcuts import render
from concert.models import Concert
from django.shortcuts import render
# Create your views here.




def index(request):
    concert_list= Concert.objects.order_by('-date')
    context = {'concert_list': concert_list}
    return render(request, 'concert/index.html', context)
