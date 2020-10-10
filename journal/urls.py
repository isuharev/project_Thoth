from django.urls import path
from .views import JournalView

urlpatterns = [
    path('', JournalView.as_view(), name='home')
]