from django.contrib import admin
from blog.models import Article, Concert

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','creation_date','update_date')

class ConcertAdmin(admin.ModelAdmin):
	list_display=('date','paf','description','place')
admin.site.register(Article,ArticleAdmin)
admin.site.register(Concert,ConcertAdmin)
