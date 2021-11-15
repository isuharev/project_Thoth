from django import forms
from .models import Entry


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class NewEntryForm(forms.ModelForm):
    number_out = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Entry
        fields = ['number_out', 'to_whom', 'what', 'executor']

    def __init__(self, *args, **kwargs):
        super(NewEntryForm, self).__init__(*args, **kwargs)


class EditEntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['number_out',
                  'to_whom',
                  'what',
                  'executor',
                  'departament',
                  ]

    def __init__(self, *args, **kwargs):
        super(EditEntryForm, self).__init__(*args, **kwargs)
