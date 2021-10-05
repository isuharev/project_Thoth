from .views import ContractsView, AddNewContactView, ContractDetailView, ContractUpdateView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


# тут прописаны URL маршруты. Благодаря им прога знает, для каких адресов какие вьюшки задействовать.
urlpatterns = [
    path('contracts/', ContractsView.as_view(), name='contract'),
    path('contracts/new/', AddNewContactView.as_view(), name='new_contract'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='detail'),
    path('contracts/<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit')
]

