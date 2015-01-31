from django.contrib import admin
from blog.models import Article #,Video,Photo



from sorl.thumbnail import get_thumbnail

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','image_tag','creation_date','update_date')

admin.site.register(Article,ArticleAdmin)
