import json
import os

from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings

listings = None
with open(os.path.join(settings.BASE_DIR, 'listings.json')) as f:
        listings = json.load(f)
        
print listings


def index(request):
	return render(request, 'rentals/templates/rentals/index.html', {})


def listings_view(request):
	return render(request, 'rentals/templates/rentals/listings.html', {'listings': listings })
