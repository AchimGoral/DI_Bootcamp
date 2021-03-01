from django.db import models

class Mission(models.Model):

    name = models.CharField(max_length=50)
    pilot = models.CharField(max_length=50, null=True)
    launch_date = models.DateField(null=True)
    training_mission = models.BooleanField(default=False)

    def __repr__(self):
        return f"Mission{self.id}: {self.name}"

    def get_pilot(self):
        return self.pilot or "No pilot selected yet"