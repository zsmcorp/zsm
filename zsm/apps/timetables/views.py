from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Timetable



def index(request):
    return render(request, 'timetables/list.html')

def class_11b(request):
    list_timetable_11b = Timetable.objects.filter(class_init = '11Б')[:10]
    return render(request, 'timetables/timetables.html', {'list_timetable_11b':list_timetable_11b})