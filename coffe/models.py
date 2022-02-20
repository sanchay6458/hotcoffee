from django.db import models
class HeaderFooter(models.Model):
    logo = models.CharField(max_length=20,null=True,blank=True)
    inst_link = models.CharField(max_length=100,null=True,blank=True)
    twitter_link = models.CharField(max_length=100,null=True,blank=True)
    ind_link = models.CharField(max_length=100,null=True,blank=True)
    com_footer = models.CharField(max_length=100,null=True,blank=True)
    comDate_footer = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.logo
class BoddySection1(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    pic = models.ImageField(null=True,blank=True,upload_to='media/images/')
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='media/images/')
    dates = models.CharField(max_length=100,null=True,blank=True)
    paragraph1 = models.TextField(null=True,blank=True)
    paragraph2 = models.TextField(null=True,blank=True)
    heading1 = models.CharField(max_length=100)
    paragraph3 = models.TextField(null=True,blank=True)
    heading2 = models.CharField(max_length=100,null=True,blank=True)
    paragraph4 = models.TextField(null=True,blank=True)
    heading3 = models.CharField(max_length=100,null=True,blank=True)
    paragraph5 = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title
class BoddySection2(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    pragraph = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='media/images/')
    dates = models.CharField(max_length=100,null=True,blank=True)
    paragraph1 = models.TextField(null=True,blank=True)
    paragraph2 = models.TextField(null=True,blank=True)
    heading1 = models.CharField(max_length=100)
    paragraph3 = models.TextField(null=True,blank=True)
    heading2 = models.CharField(max_length=100,null=True,blank=True)
    paragraph4 = models.TextField(null=True,blank=True)
    heading3 = models.CharField(max_length=100,null=True,blank=True)
    paragraph5 = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title   
class BoddySection3(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    pragraph = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='media/images/')
    dates = models.CharField(max_length=100,null=True,blank=True)
    paragraph1 = models.TextField(null=True,blank=True)
    paragraph2 = models.TextField(null=True,blank=True)
    heading1 = models.CharField(max_length=100)
    paragraph3 = models.TextField(null=True,blank=True)
    heading2 = models.CharField(max_length=100,null=True,blank=True)
    paragraph4 = models.TextField(null=True,blank=True)
    heading3 = models.CharField(max_length=100,null=True,blank=True)
    paragraph5 = models.TextField(null=True,blank=True) 
    def __str__(self):
        return self.title
    
class BoddySection4(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    pragraph = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='media/images/')
    dates = models.CharField(max_length=100,null=True,blank=True)
    paragraph1 = models.TextField(null=True,blank=True)
    paragraph2 = models.TextField(null=True,blank=True)
    heading1 = models.CharField(max_length=100)
    paragraph3 = models.TextField(null=True,blank=True)
    heading2 = models.CharField(max_length=100,null=True,blank=True)
    paragraph4 = models.TextField(null=True,blank=True)
    heading3 = models.CharField(max_length=100,null=True,blank=True)
    paragraph5 = models.TextField(null=True,blank=True) 
    def __str__(self):
        return self.title
# Create your models here.
