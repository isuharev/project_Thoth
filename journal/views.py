from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry


class JournalView(ListView):
    model = Entry
    template_name = 'home.html'
    queryset = Entry.objects.all()
