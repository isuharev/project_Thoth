from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Entry


class EntryResource(resources.ModelResource):

    class Meta:
        model = Entry


class ImportExportAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EntryResource

    # Отобразим поля модели в заголовке таблички на странице договоров (по имени полей в модели)
    list_display = ('number', 'number_out', 'reg_date', 'reg_time', 'to_whom', 'what', 'executor', 'author', 'user_ip')

    # Добавим фильтр по указанным ниже полям
    list_filter = ('executor', 'author', 'to_whom')

    # Добавим строку поиска, указав, по каким полям модели будет организован поиск
    search_fields = ('executor', 'departament', 'to_whom')

    # Добавим панель с иерархией дат, которая позволит быстро переключаться по годам
    date_hierarchy = 'reg_date'


admin.site.register(Entry, ImportExportAdmin)
