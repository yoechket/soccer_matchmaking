from django.db import models


class Slot(models.Model):
    name = models.CharField(max_length=100)

    start_play_time = models.DateTimeField()

    end_play_time = models.DateTimeField()

    def __str__(self):
        return self.name
