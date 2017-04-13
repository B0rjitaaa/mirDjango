from django.shortcuts import render
from django.http import HttpResponse

from main.models import ExceptionMessage
# Create your views here.

def index(request):
	exceptionMessages = ExceptionMessage.objects.all()
	response = {
		'exceptionMessages': exceptionMessages
	}
	return render(request, 'index.html', response)