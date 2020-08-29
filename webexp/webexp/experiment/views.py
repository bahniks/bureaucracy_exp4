from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Participant, Trial

from collections import namedtuple

import re
import json

import uuid
uuids = ['28578c95-e817-4748-ab78-1ecea968aa69', '982ee343-fca5-425b-98fb-78e446e4d67b', '23b8de0e-0c17-4500-b676-1424e13846eb', '21a52b0f-2ba3-4e61-a8e5-ddfa4bcf7f56', 'f3d4ff0b-8e0a-411e-80c0-61c33a68a3dd', 'cffed6e8-0146-40ec-84e8-49f1fb1fdc3c', '4f62e9f4-d51a-461c-a1ad-0fb1cabc2a83', '0671538e-86b8-4b5b-a7ba-d764667a929a', 'e73b7f2c-dc93-4627-9e0f-9efbf196b918', '5493ed66-4f3c-495b-87cb-c3540be7efcc', 'e00ef8b9-9eea-4571-850f-92527800345e', '82e1516b-af8d-4afc-8565-afc963cf1e4e', '3b1fc8a7-102f-41a0-a94f-c6d6f245569f', '9a683c42-8a7c-44d1-b323-6204093e8503', '6124ce62-d686-4ca2-b821-4f2c9dc5d00b', '4ded060b-6370-4b13-a0d4-c71e51186a8f', '708dcba2-acbe-4261-b2a9-d5b0aebe6ff5', 'b6a039a2-dc2e-421b-9424-8b693f4f9efb', '94474314-4f39-47b4-b796-cb31e17c2ccd', 'f5ffc78a-3ec9-4ab8-a76b-edb86de157fd', 'f0cc13b9-26cc-4821-a8d5-b3a8d1829e80', '41778b02-876f-4a42-aa1a-6193920beb84', 'e72f35c1-d269-406a-97a0-602dcb52bc3d', 'be3618e5-16e3-4d2b-aa55-6fa1c4a9ad63', 'bcd77e0b-fad7-423a-ab98-3093b53b7ff3', '9cc3b3c1-18e7-4e45-9393-4417f0459f83', '59a93ac9-7670-445e-adb8-c17b198b9318', '923b4704-dcc3-4b50-bf41-3fdd9a8f9a89', '0ff5ba74-4ba6-47ec-bff5-f5a4a2f49ab2', 'ddcee9cb-06ed-400e-9b28-f9b050ec96f0', '875b8936-5333-49f6-bcce-21fae26e6c18', 'ce1bf188-ce73-4f21-adcc-2f7effb82049', '9d92e6fd-08c7-41b3-bb08-a44b84267ada', 'df92e7df-5c9e-402d-b8f0-7102264a2e20', '788440a4-55f2-4c5e-8226-cdc416a477d2', 'de1fbbe9-a45f-492a-9072-202495b4f527', '6dc4e422-f2e2-4d9a-90a4-ccb60bcacbc6', '1d75ff5b-1fc2-49af-a602-996185f174af', 'ee11b721-bdc0-4ed3-a6da-1bbe4c25e455', 'eb99c196-6325-406a-aa4d-7b23a3c94397', '100a8bb4-8c25-40a2-9efd-105bd8e69100', '8c727d1a-df2e-4a08-90a7-e499f0c30944', '3d6a60e3-92b3-4c57-ba76-d04ea6170fd7', '3db0d72d-a20e-4361-a293-fe3e8abf073c', 'a81d0d15-08dc-453a-8bc7-d99b0a4a01ed', 'b96d31bf-606c-4db8-ae6e-e0908c481566', '91b739eb-dc34-4d7a-b0c3-912fc0e4af7e', 'dbe98ab7-e136-40ea-95f4-38e52f7dcd05', 'f1930e11-26cd-4ba1-8856-ad6910770889', '99650f3e-c60a-4dd3-85f8-c0455a7c0fea', 'e4f542b0-da68-440a-82ff-daad6066b5d4', '2b6c1771-b582-4b79-88d8-b024a325725d', '1b89e46a-3770-47de-be79-60cc8d1e993e', '7be6b0c0-4751-4fa8-ac10-cefa4a19cac7', '098bca29-3a83-46ef-97d2-a4e281f18f48', '8ea0cec6-f4c5-43ef-8c38-95c4455533fd', '2327b4a7-491d-4e83-ac14-00ca2260a7da', '3fc158d7-109d-462d-8e1d-49a2ae7245a2', 'f91660f6-bdf6-4d43-85fd-3e17e554d407', 'bf75080e-337f-40ca-bdde-116565ccbba6', '3569424b-33ad-4157-8828-646af54e9f00', '265d315c-8dfc-44c4-af3e-f56d74e89d6c', '1a56982c-a03c-48ce-bcba-6ce9b97b0584', '86bc6be7-c899-41cc-b4d4-b5127597e43a', '31148c06-1ca6-4f1f-b3d8-cc01691d2891', '8190f060-006d-44c7-8fbe-fb908b2bf959', '8389d620-ada5-4432-a7c3-68981c7d946c', 'e03251b1-8579-4d86-be2b-893e1e89eb42', '585b3597-864e-4851-bb01-d88504f89c55', 'e00737f8-7d02-459b-a47e-710bd2cea3d9', '69eaac71-25be-4cb9-b0a1-650ca449f59b', '73af91aa-e329-4e65-9f36-3bf1a3cdd6ef', 'ea8e2732-7be0-4090-8e78-ce1c24577d01', 'e80d43ea-d954-46bd-94e9-b162801d4852', '8df49720-f6f2-470d-9c51-d004ba3fca83', '97822f4e-0ce4-4d1e-bcab-11039f3ab323', '128675fa-b416-43c6-bf82-bb32ebc4ef0e', '4bfa3788-884a-42fb-8fac-0610a8922d01', '1a02ccfe-846f-4c07-a71a-a0db7e19b92d', '51e9acb5-615b-492b-896c-6b41267372db', 'd2c69fab-18f3-4d3a-9512-2259c70ed714', '972cde4d-ea71-4416-8091-8e896a2136ae', '641f2d0a-8dec-4014-b85a-536d132837ae', '164de66d-bf9e-4e48-81c5-cb258c4dfc69', 'b3dea674-eba1-499d-81a2-196478ee8bef', 'd55fd1c3-c638-4094-8c4b-a4e136ecd4fd', '1c066dac-9a7b-4aeb-abb7-5b0e9595451f', '3504f0d6-8671-410f-9e10-e923ff01ad03', '50ab0076-909e-4426-b628-76862ab36912', '99bfab7f-accd-45e1-81b5-d9090cef90ce', '9b6f70f0-ec53-4f86-819c-409a550e2a41', 'de1007df-5b1d-422b-87d5-9f15418728f6', 'ab051fb7-7ace-459e-83fc-4345fb2af745', '44873cf1-b64b-4890-a70d-cd236ee70bac', '2acca718-e435-477d-ac07-48cc0c57f061', '748d7ce3-cdc1-472e-ba01-dfa273dae1d7', 'c6826492-3a4f-416b-ad58-ce6b347f2403', 'e175a9cd-f7a1-4f1e-ad22-2ba163059817', '949ad30a-392b-449b-b75b-3b7f03c16696', '17761fe1-981b-4420-81e7-b135fad15e45']


Frame = namedtuple("Frame", ["template", "function", "context"])

count = -1
participantId = ""
context = {}
selectedCharity = ""

def manager(request, code = ""):
    # manager function
    global participantId
    global context
    global count
    if str(code) not in uuids:
        template = loader.get_template('wrong_uuid.html')
        return HttpResponse(template.render({}, request))
    elif not participantId:
        participantId = str(code)
        participant = Participant(participant_id=participantId)
        participant.save()        
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
        global selectedCharity
        selectedCharity = charity
        participant.charity = charity
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
    Frame("charity", charity, {}),
    Frame("instructions1", intro, {}),
    Frame("task", task, {"practice": 1}),
    Frame("instructions2", intro, {}),
    Frame("instructions3", intro, {"charity": selectedCharity}),
    Frame("instructions4", intro, {}),
    Frame("instructions5", intro, {}),
    Frame("instructions6", intro, {}),
    Frame("instructions7", intro, {}),
    Frame("task", task, {"practice": 0}),
    Frame("account", account, {})
    ]


