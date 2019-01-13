from django.db import models

# Create your models here.
class Popmemes(models.Model):
    """
    Create a model to define how the Popmeme objects should be stored in the
    database.
    """
     # Twiter handle
    user = models.CharField(max_length=120)
    # The most popular image on the user's timeline
    pop_img = models.CharField(max_length=120)
    # The frequency of the most popular image
    freq = models.FloatField(max_value=100., min_value=0.)

    def _str_(self):
        return self.user
