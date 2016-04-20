from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Ayyyyy")
	return render(request, 'rentals/templates/rentals/index.html', {})