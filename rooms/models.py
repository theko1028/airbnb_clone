from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
