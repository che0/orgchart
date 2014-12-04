from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from orgchart.models import Person

chart = login_required(ListView.as_view(model=Person, template_name='orgchart/chart.html'))
huge_chart = login_required(ListView.as_view(model=Person, template_name='orgchart/huge_chart.html'))

class TableView(ListView):
    template_name = 'orgchart/table.html'
    
    def get_queryset(self):
        return Person.objects.all().order_by('surname', 'name')
table = login_required(TableView.as_view())

detail = login_required(DetailView.as_view(model=Person))
