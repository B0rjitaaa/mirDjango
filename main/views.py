from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime, timedelta
import json

from main.models import ExceptionMessage


def index(request):
	response = {}
	if request.method == 'POST':
		dates = request.POST.get('daterange')
		print('El post: ', dates)

		dates_calc = getDatetimesSubstract(convert_str_to_datetime(dates[:10]), convert_str_to_datetime(dates[13:]))

		exceptionMessagesTimes = {}

		for i in range(len(dates_calc)):
			exceptionMessagesTimes[dates_calc[i]] = ExceptionMessage.objects.filter(
				date__year=dates_calc[i].year, 
				date__month=dates_calc[i].month, 
				date__day=dates_calc[i].day).count()

		response = {
			'exceptionMessagesTimes': exceptionMessagesTimes,
			'totalExceptionMessages': ExceptionMessage.objects.count()
		}
		
	return render(request, 'index.html', response)


def convert_str_to_datetime(date_str):
	datetime_object = datetime.strptime(date_str, '%m/%d/%Y')
	return datetime_object


def getDatetimesSubstract(d1, d2):
	dates_calc = []
	dates_calc.append(d1)
	dates_calc.append(d2)
	delta = d2 - d1         # timedelta
	for i in range(delta.days + 1):
		dates_calc.append(d1 + timedelta(days=i))
	return dates_calc


