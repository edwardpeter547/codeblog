from django.contrib import admin
from . models import Contact, Setting

# Register your models here.

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['sitename', 'created_by', 'company', 'website', 'email']

admin.site.register(Contact)
admin.site.register(Setting, SettingsAdmin)

