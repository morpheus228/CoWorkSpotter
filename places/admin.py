from django.contrib import admin

from .models import *


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'description', 'url', 'type', 'attributes', 'timetable', 'ymaps', 'latitude',
                    'longitude')
    list_display_links = ('id',)
    list_editable = ()
    search_fields = ('id', 'name')
    list_filter = ()


admin.site.register(Place, PlaceAdmin)
