from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

#def index(request):
#    return HttpResponse("Hello, world.")

class MainView(TemplateView):
    template_name = "intro.html"


