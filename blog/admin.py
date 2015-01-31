from django.contrib import admin
from blog.models import Article,Concert,Song
from sorl.thumbnail import get_thumbnail

class SongAdmin(admin.ModelAdmin):
        list_display=('song_title','song_tag','songCloudCode_final')

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','image_tag','creation_date','update_date')

class ConcertAdmin(admin.ModelAdmin):
	list_display=('place','date','paf')	

admin.site.register(Song,SongAdmin)
admin.site.register(Concert,ConcertAdmin)
admin.site.register(Article,ArticleAdmin)
