from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Entry
from .forms import NewEntryForm
from .services import get_next_number
from .services import get_department_name
from .services import get_some_last_model_elements
from .services import get_new_number_out
from .services import format_field_to_whom


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

    def get_context_data(self, **kwargs):
        context = super(JournalNewEntry, self).get_context_data(**kwargs)

        current = get_new_number_out(obj=Entry, request=self.request)
        context.update(out=current)
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        # Научим сайт определять отдел по префиксу исходящего номера
        obj.departament = get_department_name(obj=obj, request=self.request)

        # Считали номер последней записи и через него получим номер новой записи, чтобы передать его в поле модели
        obj.number = get_next_number(obj=Entry, department=obj.departament)

        # Сформировали окончательный вид № Исх. с учётом выбранного элемента списка индексов документов
        obj.number_out = obj.number_out.split("/")[0] + "-" + self.request.POST['document_index'] + '/' + obj.number_out.split("/")[1]

        obj.to_whom = format_field_to_whom(obj.to_whom)

        # Считаем адрес пользователя
        obj.user_ip = self.request.META.get('REMOTE_ADDR')

        obj.save()
        return super(JournalNewEntry, self).form_valid(form)
