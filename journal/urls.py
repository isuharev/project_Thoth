from django.urls import path, include
from .views import JournalView, JournalNewEntry, ContractsView, AddNewContactView
from django.contrib import admin


# тут прописаны URL маршруты. Благодаря им прога знает, для каких адресов какие вьюшки задействовать.
urlpatterns = [
    path('', JournalView.as_view(), name='home'),
    path('entry/new/', JournalNewEntry.as_view(), name='new_entry'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contracts/', ContractsView.as_view(), name='contract'),
    path('contracts/new/', AddNewContactView.as_view(), name='new_contract'),
]
admin.site.site_header = "Административная панель"
admin.site.index_title = "Управление"
