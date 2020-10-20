from django import forms

from .models import Entry


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


# тут созданы виджеты для полей даты и времени
# TODO: понять до конца, как это работает
class NewEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['number', 'reg_date', 'reg_time', 'number_out', 'to_whom', 'what', 'executor', 'author']
        widgets = {
            'reg_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(NewEntryForm, self).__init__(*args, **kwargs)
        # Виджет времени захотел работать только так. Добавить его в словарь виджетов, как дату не получилось.
        # Не знаю почему так происходит, это хренова магия.
        self.fields['reg_time'].widget = TimeInput()
