from django.contrib import admin
from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "photo"]

admin.site.register(Image, imageAdmin)



# Register your models here.
