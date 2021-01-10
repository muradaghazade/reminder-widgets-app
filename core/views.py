from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.models import Widget


class IndexView(ListView):
    model = Widget
    context_object_name = 'widgets'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
