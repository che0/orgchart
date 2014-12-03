from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orgchart.models import Person

@login_required
def chart(request):
    return render(request, 'orgchart/chart.html', {
        'people': Person.objects.all(),
    })

