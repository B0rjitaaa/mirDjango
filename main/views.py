from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from main.models import ExceptionMessage
# Create your views here.

def index(request):
	# daterangepicker_start & end
	print("el post:",request.POST.get('daterange'))
	exceptionMessages = ExceptionMessage.objects.all()
	# ExceptionMessage.objects.filter(date__range=[start, end])
	# counts = ExceptionMessage.objects.filter(date__year=dates[0].date.year).count()
	# dates = ExceptionMessage.objects.filter(date__range=[start, end]).values_list('date', flat=True).distinct()
	# >>> ExceptionMessage.objects.filter(date__year=dates[0].year, date__month=dates[0].month, date__day=dates[0].day).count()
	# crear diccionario
	exceptions = {}
	response = {
		'exceptionMessages': exceptionMessages
	}
	return render(request, 'index.html', response)


def convert_str_to_datetime(date_str):
	datetime_object = datetime.strptime(date_str, '%m/%d/%Y')
	return date


