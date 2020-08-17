from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


sequence = ["intro", "intro2", "index"]

count = 0

def intro(request):
    if request.method == 'POST':
        context = {}
        global count
        count += 1
        template = loader.get_template('{}.html'.format(sequence[count]))
        return HttpResponse(template.render(context, request))  
    else:
        template = loader.get_template('intro.html')
        context = {}
        return HttpResponse(template.render(context, request))    






