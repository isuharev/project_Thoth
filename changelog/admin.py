from django.contrib import admin
from .models import ChangeLog


class ChangeLogAdmin(admin.ModelAdmin):

    list_display = ('changed',
                    'model',
                    'user',
                    'record_id',
                    'before',
                    'after',
                    'ipaddress',
                    'action_on_model')

    readonly_fields = ('user', )
    list_filter = ('model',
                   'action_on_model')


admin.site.register(ChangeLog, ChangeLogAdmin)
