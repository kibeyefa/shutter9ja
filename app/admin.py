from django.contrib import admin
from .models import Entry, Competition, EntryImage
from import_export import resources
from import_export.admin import ExportMixin

# Register your models here.
class PhotoEntryResource(resources.ModelResource):
    class Meta:
        model = Entry
        fields = ("full_name", "phone", "instagram_username", "email") 



class PhotoEntryAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PhotoEntryResource
    list_display = ("full_name", "phone", "instagram_username", "email")

admin.site.register(Entry, PhotoEntryAdmin)

admin.site.register(EntryImage)
admin.site.register(Competition)