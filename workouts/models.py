from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=200)  # e.g. tricep dips, jumping jacks
    focus = models.CharField(max_length=200)    # e.g. arms, legs, core, flexibility, cardio...
    like = models.BooleanField()  # like or dislike
    video_id = models.CharField(max_length=100)   # Youtube video ID
    
    def __str__(self):
        return f'{self.name=} {self.focus=} {self.rating=} {self.video_id=} '

