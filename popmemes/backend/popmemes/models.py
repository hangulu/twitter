from django.db import models

# Create your models here.
class Popmemes(models.Model):
    """
    Create a model to define how the Popmeme objects should be stored in the
    database.
    """
     # Twiter handle
    user = models.CharField(max_length=120, default=None)
    # The most popular image on the user's timeline
    pop_img = models.CharField(max_length=120, default=None)
    # The frequency of the most popular image
    freq = models.FloatField(default=None)

    def _str_(self):
        return self.user
