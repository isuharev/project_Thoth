from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .forms import NewContractForm
from .models import Contract
from .utils import *
import datetime


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

    def form_valid(self, form):
        
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.departament = "Не указан"
        obj.contract_full_name = get_contract_name(obj)
        obj.save()
        return super(AddNewContactView, self).form_valid(form)


class ContractDetailView(DetailView):
    model = Contract
    form_class = NewContractForm
    template_name = 'contract_detail.html'
