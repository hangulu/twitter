from django.contrib import admin
from .models import Popmemes

class MemeAdmin(admin.ModelAdmin):
    list_display = ('user', 'pop_img', 'freq')

admin.site.register(Popmemes, MemeAdmin)
