from django.contrib import admin

from .models import Participant, Trial


admin.site.register(Participant)
admin.site.register(Trial)