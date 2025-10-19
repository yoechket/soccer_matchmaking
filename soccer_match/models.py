from django.db import models


class Slot(models.Model):
    name = models.CharField(max_length=100)

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    player_number = models.IntegerField()

    start_play_time = models.DateTimeField()

    end_play_time = models.DateTimeField()

    # for slot in slots:
    #   if self.end_time - slot.start_time > timedelta(hours=1):
    #       add_to_list(slot)
    # if len(list) >= player_number:
    #    return(list)
    # compute final time slot

    def __str__(self):
        return self.name
