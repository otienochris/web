from django.db import models

# Create your models here.

class profileContent(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField()
    """ skills = models.RadioField(
        choices = ['Angular']
    ) """
