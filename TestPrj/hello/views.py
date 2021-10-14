from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request):
    contents = r'<h1>Hello World!</h1>'
    html = r'<!DOCTYPE html><html><head></head><body>' \
           + contents \
           + r'</body></html>'
    return HttpResponse(html)