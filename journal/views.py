from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Entry
from .forms import NewEntryForm
from .services import get_current_number
from .services import get_department_name
from .services import get_some_last_model_elements


class JournalView(ListView):
    """
    Вьюшка для главной странички журнала, на которой отображается табличка из базы.
    """
    model = Entry
    template_name = 'home.html'
    queryset = get_some_last_model_elements(obj=Entry, begin=0, end=50)


class JournalNewEntry(CreateView):
    """
    Вьюшка для формы, при помощи которой в журнал добавляется новая запись.
    """
    model = Entry
    form_class = NewEntryForm
    template_name = 'new_entry.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        # Считали номер последней записи и через него получим номер новой записи, чтобы передать его в поле модели
        obj.number = get_current_number(obj=Entry)

        # Научим сайт определять отдел по префиксу исходящего номера
        obj.departament = get_department_name(obj=obj, request=self.request)

        user_ip = self.request.META.get('REMOTE_ADDR')  # Считаем адрес пользователя
        obj.save()
        return super(JournalNewEntry, self).form_valid(form)
