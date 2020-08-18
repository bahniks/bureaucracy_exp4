from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Participant


sequence = ["intro3", "intro", "intro2", "index"]

count = 0

def intro(request):
    if request.method == 'POST':
        #try:
        answer = request.POST['text']
        participant = Participant(answer=answer)
        participant.save()
        #except:
        #    pass
        context = {}
        global count
        count += 1
        template = loader.get_template('{}.html'.format(sequence[count]))
        return HttpResponse(template.render(context, request))  
    else:
        template = loader.get_template('{}.html'.format(sequence[count]))
        context = {}
        return HttpResponse(template.render(context, request))    






