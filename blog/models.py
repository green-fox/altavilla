from django.db import models
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
# Create your models here.
from sorl.thumbnail import ImageField
import re


class Song(models.Model):
	song_title=models.CharField(max_length=100)
	songCloudCode=models.TextField(max_length=2000)
        songCloudCode_final =models.TextField(editable=False)
	def save(self, force_insert=False, force_update=False):
		self.songCloudCode_final = re.sub(r'<iframe.{0,}api.soundcloud.com/', '',self.songCloudCode)
		self.songCloudCode_final = re.sub(r'&amp.{0,}</iframe>','',self.songCloudCode_final)
        	super(Song, self).save(force_insert, force_update)
	def song_tag(self):
		return "<iframe width=\"100%\" height=\"166\" scrolling=\"no\" frameborder=\"no\" src=\"https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/"+self.songCloudCode_final+"&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true\"></iframe>"
        song_tag.short_description = 'view'
        song_tag.allow_tags = True



class Article(models.Model):

        title=models.CharField(max_length=50)
        description=models.TextField(max_length=2500,blank=True)
        creation_date=models.DateTimeField(auto_now_add=True)
	update_date=models.DateTimeField(auto_now=True)
	video_code=models.CharField(max_length=2500,blank=True)
	upload = ImageField()
	height= models.IntegerField(default=30)
        width= models.IntegerField(default=30)
        def image_tag(self):
                return u'<img src="/media/%s"  height="80" width="80"/>' % self.upload
        image_tag.short_description = 'Image'
        image_tag.allow_tags = True


	
class Concert(models.Model):

	date=models.DateTimeField(verbose_name="Date du concert (*) :")
	paf=models.DecimalField(verbose_name="Prix place  :",max_digits=5,decimal_places=0,blank=True,null=True)

	description=models.CharField(verbose_name="Details (*) :",max_length=50)
	place=models.CharField(verbose_name="Lieu (*) :",max_length=50)
	models.help_text="Enter the minimum (inclusive) value for this concept."
	def __unicode__(self):
		return self.description	


class Group_member(models.Model):
	name = models.CharField(max_length=50)
	descritpion = models.TextField(max_length=1000)
	picture = ImageField()
        def picture_tag(self):
                return u'<img src="/media/%s"  height="80" width="80"/>' % self.picture
        picture_tag.short_description = 'Image'
        picture_tag.allow_tags = True
