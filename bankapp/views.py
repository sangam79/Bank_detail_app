from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .models import Indianbank

class HomeView(TemplateView):
    template_name = 'index.html'

class DisplayView(ListView):
    model = Indianbank
    template_name = 'display.html'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('userinput')
        object_list = Indianbank.objects.filter(Q(ifsc__icontains = query) | Q(bank_name__icontains = query) | Q(city__icontains = query))
        return object_list
    
     



