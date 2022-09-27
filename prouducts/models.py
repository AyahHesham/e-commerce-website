from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.
#one for user and one for database
prouduct_flag=[
    ('new','new'),
    ('sold','sold'),
    ('features','features'),
]
class items(models.Model):
    name=models.CharField(verbose_name=_('Name'), max_length=50)
    flag=models.CharField(_('Flag'),choices=prouduct_flag,max_length=10)
    price=models.FloatField(_('Price'))
    sku=models.IntegerField(_('Sku'))
    subtitle=models.CharField(verbose_name=_('subtitle'), max_length=500)
    tag=TaggableManager()
    vedio=models.URLField(_('vedio'),null=True,blank=True)
    cateogry=models.ForeignKey('cateogry',verbose_name=_('cateogry'),related_name='cateogry_item',on_delete=models.SET_NULL,null=True,blank=True)
    brand=models.ForeignKey('brand',verbose_name=_('brand'),related_name='brand_item',on_delete=models.SET_NULL,null=True,blank=True)
    itemimage=models.ImageField(_('Image'),upload_to='items')
    def __str__(self) -> str:
        return self.name

class cateogry(models.Model):
    name=models.CharField(verbose_name=_('Name'), max_length=50)
    image=models.ImageField(_('Image'),upload_to='cateogry')
    def __str__(self) -> str:
        return str(self.name)

class brand(models.Model):
    name=models.CharField(verbose_name=_('Name'), max_length=50)
    image=models.ImageField(_('Image'),upload_to='brand')
    def __str__(self) -> str:
        return str(self.name)

class review(models.Model):
    user=models.ForeignKey(User,verbose_name=_('user'), related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ImageField(_('Image'),upload_to='reviwe')
    rate=models.IntegerField(_('rate'))
    review_content=models.CharField(_('reveiwcontent'),max_length=500)
    timeofreview=models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.product

class itemimages(models.Model):
    items=models.ForeignKey('items',verbose_name=_('itemimage'),related_name='image_item',on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(_('Image'),upload_to='itemimages')
    def __str__(self) -> str:
        return str(self.items)
        