from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
#static information about the company
class company(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='company')
    subtitle=models.TextField(max_length=200)
    fblink=models.URLField(null=True,blank=True)
    twlink=models.URLField(null=True,blank=True)
    linkedinlink=models.URLField(null=True,blank=True)
    intalink=models.URLField(null=True,blank=True)
    pintrestlink=models.URLField(null=True,blank=True)
    email=models.EmailField()
    #char beacuse there are signs
    callus=models.CharField(max_length=50)
    adress=models.TextField(max_length=200)
    def __str__(self) -> str:
        return self.name

