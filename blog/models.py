from django.db import models
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
# Create your models here.




class Article(models.Model):

        title=models.CharField(max_length=50)
        description=models.TextField(max_length=2500,blank=True)
        creation_date=models.DateTimeField(auto_now_add=True)
	update_date=models.DateTimeField(auto_now=True)
	video_code=models.CharField(max_length=2500,blank=True)
	upload= models.ImageField(upload_to='images/',blank=True)
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



class Concert(models.Model):

	date=models.DateTimeField(verbose_name="Date du concert :")
	paf=models.DecimalField(verbose_name="Prix de l'entrée:",max_digits=5,decimal_places=0,default=0)
	description=models.CharField(verbose_name="Details :",max_length=50)
	place=models.CharField(verbose_name="Lieu  :",max_length=50)
	models.help_text="Enter the minimum (inclusive) value for this concept."
	def __unicode__(self):
		return self.description	

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
