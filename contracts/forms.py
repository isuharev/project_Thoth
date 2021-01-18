from django import forms
from .models import Contract


class NewContractForm(forms.ModelForm):
    number_out = forms.CharField(max_length=64)

    class Meta:
        model = Contract
        fields = ['contract_date', 'departament', 'contract_index']

    def __init__(self, *args, **kwargs):
        super(NewContractForm, self).__init__(*args, **kwargs)