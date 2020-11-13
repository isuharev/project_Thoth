from django import forms
from .models import Entry


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


# тут созданы виджеты для полей даты и времени
# TODO: понять до конца, как это работает
class NewEntryForm(forms.ModelForm):
    number_out = forms.CharField(max_length=64)

    class Meta:
        model = Entry
        fields = ['number_out', 'to_whom', 'what', 'executor']

    def __init__(self, *args, **kwargs):
        super(NewEntryForm, self).__init__(*args, **kwargs)
