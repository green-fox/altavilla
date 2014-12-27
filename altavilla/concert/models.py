from django.db import models

# Create your models here.


class Concert(models.Model):

	date=models.DateTimeField(verbose_name="Date du concert (*) :")
#	datetime.widget = forms.SpdlitDateTimeWidget(time_format=('%H:%M'))
	paf=models.DecimalField(verbose_name="Prix place  :",max_digits=5,decimal_places=0,blank=True,null=True)

	description=models.CharField(verbose_name="Details (*) :",max_length=50)
	place=models.CharField(verbose_name="Lieu (*) :",max_length=50)
	models.help_text="Enter the minimum (inclusive) value for this concept."
	def __unicode__(self):
		return self.description	
