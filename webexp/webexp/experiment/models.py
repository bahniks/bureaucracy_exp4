from django.db import models


class Participant(models.Model):
    participant_id = models.CharField(max_length=50)
    charity = models.CharField(max_length=50, default="NA")
    def __str__(self):
        return self.participant_id


class Trial(models.Model):
    participant_id = models.CharField(max_length=50)
    order = models.CharField(max_length=3)	
    time_screen = models.CharField(max_length=50)	
    time_previous = models.CharField(max_length=50)
    shape = models.CharField(max_length=10)	
    color = models.CharField(max_length=10)	
    bribe = models.CharField(max_length=6)	
    response_shape = models.CharField(max_length=10)	
    response_color = models.CharField(max_length=10)	
    correct_shape = models.CharField(max_length=10)	
    correct_color = models.CharField(max_length=10)	
    charity_total = models.CharField(max_length=6)
    reward_total = models.CharField(max_length=6)	
    response_number = models.CharField(max_length=1)		
    color1 = models.CharField(max_length=10)	
    color2 = models.CharField(max_length=10)	
    color3 = models.CharField(max_length=10)	
    shape1 = models.CharField(max_length=10)	
    shape2 = models.CharField(max_length=10)	
    shape3 = models.CharField(max_length=10)
    condition = models.CharField(max_length=10, default = "NA")