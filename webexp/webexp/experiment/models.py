from django.db import models


class Participant(models.Model):
    #participant_id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=200)
    def __str__(self):
        return self.answer