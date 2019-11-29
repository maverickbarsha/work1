from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
    )

from .models import T

class TList(ListView):
    model = T

class TCreate(CreateView):
    model = T
    success_url = reverse_lazy('t_list')
    fields = ['username', 'tname', 'des']

class TUpdate(UpdateView):
    model = T
    success_url = reverse_lazy('t_list')
    fields = [ 'username', 'tname', 'des']

class TDelete(DeleteView):
    model = T
    success_url = reverse_lazy('t_list')
