from django.urls import path, include
from .views import JournalView, JournalNewEntry, JournalDetailView, EntryUpdateView
from django.contrib import admin


# тут прописаны URL маршруты. Благодаря им прога знает, для каких адресов какие вьюшки задействовать.
urlpatterns = [
    path('', JournalView.as_view(), name='home'),
    path('entry/new/', JournalNewEntry.as_view(), name='new_entry'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('entry/<int:pk>/', JournalDetailView.as_view(), name='journal_detail'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit')
]
admin.site.site_header = "Административная панель"
admin.site.index_title = "Управление"
