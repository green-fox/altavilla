from django.contrib import admin
from blog.models import Article,Concert
from sorl.thumbnail import get_thumbnail

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','image_tag','creation_date','update_date')

class ConcertAdmin(admin.ModelAdmin):
	list_display=('place','date','paf')	


admin.site.register(Concert,ConcertAdmin)
admin.site.register(Article,ArticleAdmin)
