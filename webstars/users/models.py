from django.db import models


# Create your models here.


class userRegistration(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()

class
    