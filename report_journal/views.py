from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import Reports
from .forms import NewReportForm
import datetime


class ReportsView(ListView):

    model = Reports
    template_name = 'reports.html'
    queryset = model.objects.all().order_by('-id')


class AddNewReportView(CreateView):
    model = Reports
    form_class = NewReportForm
    template_name = 'new_report.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(AddNewReportView, self).form_valid(form)
