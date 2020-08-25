from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Participant, Trial

from collections import namedtuple

import re
import json

Frame = namedtuple("Frame", ["template", "function", "context"])

count = -1
participantId = ""
context = {}

def manager(request):
    # manager function
    global context
    global count
    if request.method == 'POST':
        if sequence[count].function(request):
            # do not proceed to the next frame if returns True
            count -= 1
    count += 1
    context = sequence[count].context
    template = loader.get_template('{}.html'.format(sequence[count].template))
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


def account(request):
    # bank account information
    try:
        # checking the provided bank account number
        codes = ['0100', '0300', '0600', '0710', '0800', '2010', '2020', '2030', '2060', '2070', '2100', '2200', '2220', '2240', '2250', '2260', '2275', '2600', '2700', '3030', '3050', '3060', '3500', '4000', '4300', '5500', '5800', '6000', '6100', '6200', '6210', '6300', '6700', '6800', '7910', '7940', '7950', '7960', '7970', '7980', '7990', '8030', '8040', '8060', '8090', '8150', '8200', '8215', '8220', '8225', '8230', '8240', '8250', '8255', '8260', '8265', '8270', '8280', '8290', '8291', '8292', '8293', '8294', '8295', '8296', '8297', '8298']
        providedNumber = request.POST['account'].strip()
        pattern = re.findall(r'^(?:([0-9]{1,6})-)?([0-9]{2,10})\/([0-9]{4})$', providedNumber)
        if not pattern:
            # email?
            if not re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', providedNumber):
                raise Exception(f"Zadané číslo {providedNumber} nemá správný formát.")
        else:
            weights = [6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
            prefix = pattern[0][0].rjust(10, "0")
            main = pattern[0][1].rjust(10, "0")
            bank = pattern[0][2]
            checksum = sum([weights[i] * int(prefix[i]) for i in range(len(prefix))])
            if checksum % 11 != 0:
                raise Exception(f"Zadané číslo {providedNumber} je chybné.")
            checksum = sum([weights[i] * int(main[i]) for i in range(len(prefix))])
            if checksum % 11 != 0:
                raise Exception(f"Zadané číslo {providedNumber} je chybné.")
            if bank not in codes:
                raise Exception(f"Kód banky {bank} v zadaném čísle {providedNumber}  je chybný.")
        # adding the number in the database
        global participantId
        participant = Participant.objects.get(participant_id = participantId) # pylint: disable=no-member
        participant.bank_account = providedNumber
        participant.save()
    except Exception as e:
        print(e)    
        global context
        context["exception"] = e
        return True


def task(request):
    # the task itself
    try:
        data = json.loads(request.body.decode("utf-8"))
        end = data.pop("lastTrial")
        if end:
            global participantId
            participant = Participant.objects.get(participant_id = participantId) # pylint: disable=no-member
            participant.reward = data['reward_total']
            participant.charity_reward = data['charity_total']
            participant.save()
        trial = Trial(participant_id=participantId, **data)
        trial.save()
    except Exception as e:
        print(e)
    return not end


def intro(request):
    # frames showing only instructions
    pass


sequence = [
    Frame("intro", intro, {}),
    Frame("validator", validate, {}),
    Frame("charity", charity, {}),
    Frame("instructions1", intro, {}),
    Frame("instructions4", intro, {}),
    Frame("task", task, {"practice": 1}),
    Frame("task", task, {"practice": 0}),
    Frame("account", account, {})
    ]

sequence = [Frame("task", task, {"practice": 0})] * 50


