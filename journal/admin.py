from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Entry


class EntryResource(resources.ModelResource):

    class Meta:
        model = Entry


class ImportExportAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EntryResource


admin.site.register(Entry, ImportExportAdmin)
