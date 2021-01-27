from .views import ContractsView, AddNewContactView, ContractDetailView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


# тут прописаны URL маршруты. Благодаря им прога знает, для каких адресов какие вьюшки задействовать.
urlpatterns = [
    path('contracts/', ContractsView.as_view(), name='contract'),
    path('contracts/new/', AddNewContactView.as_view(), name='new_contract'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='detail')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
