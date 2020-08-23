from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Participant, Trial

from collections import namedtuple

import json

Frame = namedtuple("Frame", ["template", "function"])

count = -1
participantId = ""

def manager(request):
    # manager function
    global count
    if request.method == 'POST':
        if sequence[count].function(request):
            # do not proceed to the next frame if returns True (just in the task)
            count -= 1
    count += 1
    template = loader.get_template('{}.html'.format(sequence[count].template))
    context = {}
    return HttpResponse(template.render(context, request)) 


def charity(request):
    # charity selection
    try:
        global participantId
        participant = Participant.objects.get(participant_id = participantId) # pylint: disable=no-member
        charity = request.POST['charity']
        participant.charity = charity
        participant.save()
    except Exception as e:
        print(e)    
      

def validate(request):
    # creating participant in the database
    try:
        global participantId
        participantId = request.POST['text']
        participant = Participant(participant_id=participantId)
        participant.save()
    except Exception as e:
        print(e)


def task(request):
    # the task itself
    try:
        data = json.loads(request.body.decode("utf-8"))
        end = data.pop("lastTrial")
        trial = Trial(participant_id=participantId, **data)
        trial.save()
    except Exception as e:
        print(e)
    return not end


def intro(request):
    # frames showing only instructions
    pass


sequence = [
    Frame("intro", intro),
    Frame("validator", validate),
    Frame("charity", charity),
    Frame("instructions1", intro),
    Frame("instructions4", intro),
    Frame("task", task)
    ]

sequence = [
    Frame("validator", validate),
    Frame("task", task),
    Frame("instructions1", intro)
    ]


