from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from utils.genrate_code import genrate_code
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
'''
we will use 'one to one model' method 
django user had 
firstname-lastname-passowrd-email
'''
class profile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='users')
#create activation code for every profile by use func for genrate code using random model this func in another file to use it in other files
# will hide after activate
    code=models.CharField(max_length=10,default=genrate_code)
#code used for confirm if user used thie code or not,will be true for if user wanna make other code not repeate
    code_user=models.BooleanField(default=False)
#if user made any probem and i wanna to diactive them i will make that by active by make it false
    active= models.BooleanField(default=False)

#after save user call this fun
@receiver(post_save,sender=User)
# fun for after add user create profile for him
# sender: who send signal , instance : data ,kwarges : for recive any num from parameters
# every user make sign up return parameter equal true if that return we will create profile if not the user edite their profile
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)


data_types=(
    ('home','home'),
    ('academy','academy'),
    ('office','office'),
    ('other','others'),
)

class contact(models.Model):
    user=models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE) 
    phone=models.CharField(max_length=15)
    type=models.CharField(choices=data_types,max_length=10)

class user_adress(models.Model):
    user=models.ForeignKey(User,related_name='user_adress',on_delete=models.CASCADE) 
    type=models.CharField(choices=data_types,max_length=10)
    '''we will use django country that had all countries in the world'''
    country=CountryField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    region=models.CharField(max_length=30)
    street=models.CharField(max_length=80 )
    notes=models.CharField(max_length=250)
       
