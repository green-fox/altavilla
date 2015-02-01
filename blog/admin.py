from django.contrib import admin
from blog.models import Article,Concert,Song,Group_member, Carousel
from sorl.thumbnail import get_thumbnail

class SongAdmin(admin.ModelAdmin):
        list_display=('song_title','song_tag','songCloudCode_final')

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','image_tag','creation_date','update_date')

class Group_memberAdmin(admin.ModelAdmin):
        list_display=('name','picture_tag')


class ConcertAdmin(admin.ModelAdmin):
	list_display=('place','date','paf')
	
class CarouselAdmin(admin.ModelAdmin):
        list_display=('picture_tag',)

admin.site.register(Song,SongAdmin)
admin.site.register(Group_member,Group_memberAdmin)
admin.site.register(Concert,ConcertAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Carousel,CarouselAdmin)

