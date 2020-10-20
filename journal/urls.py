from django.urls import path
from .views import JournalView, JournalNewEntry


# тут прописаны URL маршруты. Благодаря им прога знает, для каких адресов какие вьюшки задействовать.
urlpatterns = [
    path('', JournalView.as_view(), name='home'),
    path('entry/new/', JournalNewEntry.as_view(), name='new_entry')
]
