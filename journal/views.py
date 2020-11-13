from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Entry
from .forms import NewEntryForm


class JournalView(ListView):
    """
    Вьюшка для главной странички журнала, на которой отображается табличка из базы.
    """
    model = Entry
    template_name = 'home.html'
    queryset = Entry.objects.all().order_by('-id')


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

        n = Entry.objects.all().order_by('-id')
        obj.number = n[0].number + 1

        # Научим сайт определять отдел по префиксу исходящего номера
        chk = obj.number_out.split("/")
        if chk[0] == "155":
            obj.departament = "Геодинамики"
        elif chk[0] == "156":
            obj.departament = "Гравиметрии"
        else:
            # Если по префиксу распознать не удаётся, то пробуем считать название отдела по имени группы
            try:
                obj.departament = self.request.user.groups.get().name
            except:
                # Если группа не указана, присвоим значение по умолчанию
                obj.departament = "не указан"
        print(">>>Entry added by ip:", self.request.META.get('REMOTE_ADDR'))
        obj.save()
        return super(JournalNewEntry, self).form_valid(form)
