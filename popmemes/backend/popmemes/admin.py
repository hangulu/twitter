from django.contrib import admin
from .models import PopImage

class MemeAdmin(admin.ModelAdmin):
    list_display = ('user', 'pop_img', 'freq')

admin.site.register(PopImage, MemeAdmin)
