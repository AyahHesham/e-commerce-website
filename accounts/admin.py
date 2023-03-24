from django.contrib import admin

# Register your models here.
from .models import profile , user_adress, contact

admin.site.register(profile)
admin.site.register(user_adress)
admin.site.register(contact)