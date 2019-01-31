from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
  template = loader.get_template('search/index.html')
  return HttpResponse(template.render({}, request))

def results_postback(request):
  search_term = request.POST['search_term']
  return redirect('results', search_term=search_term)

def results(request, search_term):
  template = loader.get_template('search/results.html')
  return HttpResponse(template.render({
    'search_term': search_term
  }, request))