from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.shortcuts import render
from .forms import NewContractForm
from .models import Contract


# TODO!!!!!! Это заглушки для отображения таблицы договоров и формы добавления договора
# TODO их нужно будет наполнить собственной логикой
class ContractsView(ListView):

    model = Contract
    template_name = 'contracts.html'
    queryset = model.objects.all().order_by('-id')


class AddNewContactView(CreateView):
    model = Contract
    form_class = NewContractForm
    template_name = 'new_contract.html'
