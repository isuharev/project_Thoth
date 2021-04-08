from .models import Reports
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class NewReportForm(forms.ModelForm):

    class Meta:
        model = Reports
        fields = ['number',
                  'date',
                  'doc_number',
                  'doc',
                  'from_to',
                  'what',
                  'comment']
        widgets = {
            'date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(NewReportForm, self).__init__(*args, **kwargs)
