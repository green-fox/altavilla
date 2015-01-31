from django.db import models
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
# Create your models here.
from sorl.thumbnail import ImageField



class Article(models.Model):

        title=models.CharField(max_length=50)
        description=models.TextField(max_length=2500,blank=True)
        creation_date=models.DateTimeField(auto_now_add=True)
	update_date=models.DateTimeField(auto_now=True)
	video_code=models.CharField(max_length=2500,blank=True)
#	upload= models.ImageField(upload_to='images/',blank=True)
	upload = ImageField()

        def image_tag(self):
                return u'<img src="/images/%s"  height="80" width="80"/>' % self.image
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
