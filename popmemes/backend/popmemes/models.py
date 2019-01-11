from django.db import models

# Create your models here.
class Popmemes(models.Model):
    user = models.CharField(max_length=120)

    def _str_(self):
        return self.user
