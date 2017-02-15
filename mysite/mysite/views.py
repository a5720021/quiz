from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse ,Http404

def index(request):
    return HttpResponse('<h1>Fill your name.</h1><br><input type="text" name="name"><br><br><input type="submit">'
) 
