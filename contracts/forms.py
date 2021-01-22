from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import Contract
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class NewContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ['contract_date',
                  'departament_code',
                  'contract_index',
                  'contract_date',
                  'number',
                  'executor',
                  'contract_cost',
                  'contract_status']
        widgets = {
            'contract_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(NewContractForm, self).__init__(*args, **kwargs)
