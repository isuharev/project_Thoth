from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView
from .forms import NewContractForm, EditContractForm
from .models import Contract
from .utils import *


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
        print(obj.contract_date)
        obj.contract_full_name = get_contract_name(obj)
        # obj.save()
        return super(AddNewContactView, self).form_valid(form)


class ContractDetailView(DetailView):
    model = Contract
    form_class = NewContractForm
    template_name = 'contract_detail.html'


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = EditContractForm
    template_name = 'contract_edit.html'

    def get_context_data(self, **kwargs):
        context = super(ContractUpdateView, self).get_context_data(**kwargs)
        # print(self.request.path)
        id = self.request.path.split("/")[2]
        # print(id)
        cur_contract = Contract.objects.get(pk=id)
        # print(cur_contract.contract_date)
        cur_date = cur_contract.contract_date
        current = str(cur_date)
        context.update(out=current)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.contract_full_name = get_contract_name(obj)
        # obj.save()
        return super(ContractUpdateView, self).form_valid(form)
