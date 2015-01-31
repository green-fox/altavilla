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
                self.songCloudCode_final = re.sub(r'playlists/','',self.songCloudCode_final)
                self.songCloudCode_final = re.sub(r'trackss/','',self.songCloudCode_final)
		self.songCloudCode_final = re.sub(r'&amp.{0,}</iframe>','',self.songCloudCode_final)
        	super(Song, self).save(force_insert, force_update)
	def song_tag(self):
                return u'%s' % self.songCloudCode
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


	def delete(self, *args, **kwargs):
		try:
	    		
			# You have to prepare what you need before delete the model
	        	storage, path = self.upload.storage, self.upload.path
			print(" 1: self.upload.storage, self.upload.path")
		except:
			print ("exception 1 : no_file attached")
			# Delete the model before the file
			
		try:
			
		 	super(Article, self).delete(*args, **kwargs)
			print(" 2: delete the article super ")
	        	#super(Article, self).delete.title
			# Delete the file after the model
		except:
			print("exception 2 : super")
			
		try:
	        	storage.delete(path)
			print("3: remove")
		except:
			print("exception 3 : remove failed")
	def __unicode__(self):
		return self.title
#def delete_file_field(sender, **kwargs):
#    print("delete in progress")
#    """Automatically deleted files when records removed.
#    
#    On Django 1.3, removing records will not followed by deleting files.
#    Should manually delete PDF using signals post_delete.
#    """
#    image = kwargs.get('instance')
#    #default_storage.delete(image.upload.path)
#    #image.storage.delete(image.upload.path)
#    default_storage.delete(image.upload.path)
#post_delete.connect(delete_file_field, Article)


def delete_file_field(sender, **kwargs):
    print("delete in progress")
    try: 
	image = kwargs.get('instance')
    #default_storage.delete(image.upload.path)
    #image.storage.delete(image.upload.path)
	image.delete(image.upload.path)
    except :
	print("bulk delete no file to delete")
post_delete.connect(delete_file_field, Article)




class Concert(models.Model):

	date=models.DateTimeField(verbose_name="Date du concert (*) :")
#	datetime.widget = forms.SpdlitDateTimeWidget(time_format=('%H:%M'))
	paf=models.DecimalField(verbose_name="Prix place  :",max_digits=5,decimal_places=0,blank=True,null=True)

	description=models.CharField(verbose_name="Details (*) :",max_length=50)
	place=models.CharField(verbose_name="Lieu (*) :",max_length=50)
	models.help_text="Enter the minimum (inclusive) value for this concept."
	def __unicode__(self):
		return self.description	
