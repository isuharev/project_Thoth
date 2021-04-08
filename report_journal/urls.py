from .views import ReportsView, AddNewReportView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


# тут прописаны URL маршруты. Благодаря им прога знает, для каких адресов какие вьюшки задействовать.
urlpatterns = [
    path('reports/', ReportsView.as_view(), name='reports'),
    path('reports/new/', AddNewReportView.as_view(), name='new_report'),
]
