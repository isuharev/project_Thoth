from django.contrib import admin
from .models import Contract


class PostAdmin(admin.ModelAdmin):

    # Отобразим поля модели в заголовке таблички на странице договоров (по имени полей в модели)
    list_display = ('contract_full_name', 'contract_date', 'executor', 'author', 'registration_date')

    # Добавим фильтр по указанным ниже полям
    list_filter = ('contract_date', 'executor', 'author', 'contract_status')

    # Добавим строку поиска, указав, по каким полям модели будет организован поиск
    search_fields = ('executor', 'contract_status', 'author')

    # Добавим панель с иерархией дат, которая позволит быстро переключаться по годам
    date_hierarchy = 'contract_date'


admin.site.register(Contract, PostAdmin)
