from django.contrib import admin
from . models import Sites, Guard
# Register your models here.



@admin.register(Guard)
class GuardAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active', 'site_locations')
    filter_horizontal = ('sites',)
    
    def site_locations(self, obj):
        return ", ".join(
            site.location for site in obj.sites.all()
        )
    
    site_locations.short_description = "Site Locations"
    
@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)