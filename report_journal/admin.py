from django.contrib import admin
from .models import Reports


class PostAdmin(admin.ModelAdmin):

    # Отобразим поля модели в заголовке таблички на странице договоров (по имени полей в модели)
    list_display = ('number', 'date', 'doc_number', 'doc', 'from_to', 'what', 'author')

    # Добавим фильтр по указанным ниже полям
    list_filter = ('date', 'from_to', 'author')

    # Добавим строку поиска, указав, по каким полям модели будет организован поиск
    search_fields = ('doc', 'doc_number', 'what', 'from_to')

    # Добавим панель с иерархией дат, которая позволит быстро переключаться по годам
    date_hierarchy = 'date'


admin.site.register(Reports, PostAdmin)
