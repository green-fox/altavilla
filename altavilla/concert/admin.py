from django.contrib import admin
from concert.models import Concert
# Register your models here.


##
###
# This class is to sort and  define the fiel to
# show in the admin page
###
##


class ConcertAdmin(admin.ModelAdmin):
	list_display=('place','date','paf')	


admin.site.register(Concert,ConcertAdmin)
