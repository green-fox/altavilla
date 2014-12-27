from django.contrib import admin
from blog.models import Article #,Video,Photo
# Register your models here.
#admin.site.register(Video)
#admin.site.register(Photo)

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','creation_date','update_date')

admin.site.register(Article,ArticleAdmin)
