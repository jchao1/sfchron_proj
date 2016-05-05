import json
import os

from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings

listings = None
with open(os.path.join(settings.BASE_DIR, 'listings.json')) as f:
        listings = json.load(f)

roommates = None
with open(os.path.join(settings.BASE_DIR, 'roommates.json')) as f:
        roommates = json.load(f)

def index(request):
	return render(request, 'rentals/templates/rentals/index.html', {})

def listings_view(request):
	return render(request, 'rentals/templates/rentals/listings.html', {'listings': listings })

def roommates_view(request):
	return render(request, 'rentals/templates/rentals/roommates.html', {'roommates': roommates })

def openhouse_view(request):
	return render(request, 'rentals/templates/rentals/openhouse.html', {'listings': listings })

def profile_view(request):
	return render(request, 'rentals/templates/rentals/profile.html', {})

def property_view(request, id):
	return render(request, 'rentals/templates/rentals/property.html', {'listings': listings, 'listingID': int(id) })

def user_view(request, id):
	return render(request, 'rentals/templates/rentals/user.html', {'roommates': roommates, 'userID': int(id) })
	