from pyexpat import model
from django.contrib import admin
from .models import cateogry,items,brand,review,itemimages
#بربطه بكلاس الصور 
class itemimagesinline(admin.TabularInline):
    model=itemimages
    
class productadmin(admin.ModelAdmin):
    list_display=['name','price']
    inlines=[itemimagesinline]


admin.site.register(cateogry)
admin.site.register(items,productadmin)
admin.site.register(brand)
admin.site.register(review)
admin.site.register(itemimages)



# Register your models here.
