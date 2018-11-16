from django.shortcuts import render
from .models import Schedule


def index(request):
    schedules = Schedule.objects.all()
    return render(request, 'bb_schedule/index.html', {
        'schedules': schedules,
    })