from django.contrib import admin

from .models import *


class TgUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'created_at')
    list_display_links = ('id', 'username')
    list_editable = ()
    search_fields = ('id', 'username')
    list_filter = ()


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url', 'type', 'attributes', 'working_hours', 'ymap', 'latitude',
                    'longitude')
    list_display_links = ('id',)
    list_editable = ()
    search_fields = ('id', 'name')
    list_filter = ()


admin.site.register(TgUser, TgUserAdmin)
admin.site.register(Place, PlaceAdmin)
