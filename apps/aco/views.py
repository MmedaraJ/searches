from email import message
from django.shortcuts import redirect, render, reverse, HttpResponse
import requests

def index(request):
    return render(request, 'aco/index.html')

def fetch(request):
    artist = request.POST['artist'].replace(' ', '')
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
    # notice this is 'requests' not 'request'
    # we are using the requests module 'get' function to send a request from our server
    # then we use ".content" to get the content we are looking for
    response = requests.get(url).content
    # we then send the response back to our template which sent the initial post request
    # we don't jsonify it as it is already in JSON format!
    return HttpResponse(response, content_type='application/json')