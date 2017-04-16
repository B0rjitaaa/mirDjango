from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
import json

from main.models import ExceptionMessage

def index(request):
	exceptionMessages = ExceptionMessage.objects.all()
	response = {
			'exceptionMessages': exceptionMessages
		}
	if request.method == 'POST':
		dates = request.POST.get('daterange')
		print('El post: ', dates)
		exceptionMessages = ExceptionMessage.objects.all()

		#Retrieving dates from DB
		dates_filtered = ExceptionMessage.objects.filter(date__range=[convert_str_to_datetime(dates[:10]), convert_str_to_datetime(dates[13:])]).values_list('date', flat=True).distinct()

		#Count same dates --> date1:3 times .eg
		exceptionMessagesTimes = {}
		for i in range (len(dates_filtered)):
			date_aux = str(dates_filtered[i].year) + '/' + str(dates_filtered[i].month) + '/' + str(dates_filtered[i].day)
			exceptionMessagesTimes[date_aux] = ExceptionMessage.objects.filter(
				date__year=dates_filtered[i].year, 
				date__month=dates_filtered[i].month, 
				date__day=dates_filtered[i].day).count()

		response = {
			'exceptionMessagesTimes': exceptionMessagesTimes
		}

		print("ExceptionMessagestimes: ", exceptionMessagesTimes)
		

	return render(request, 'index.html', response)


def convert_str_to_datetime(date_str):
	datetime_object = datetime.strptime(date_str, '%m/%d/%Y')
	return datetime_object


