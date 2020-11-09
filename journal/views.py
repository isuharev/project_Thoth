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
        try:
            obj.departament = self.request.user.groups.get().name
        except:
            obj.departament = "не указан"
        print(">>>Entry added by ip:", self.request.META.get('REMOTE_ADDR'))
        obj.save()
        return super(JournalNewEntry, self).form_valid(form)
