from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    STATE_CHOICES = (
        ('florida', 'Florida'),
        ('texas', 'Texas'),
        ('california', 'California'))

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)
    state = models.CharField(max_length=255, choices=STATE_CHOICES, null=True)

    class Meta:
        verbose_name_plural = "Cities"


class Restaurant(models.Model):
    RESTAURANT_CHOICES = (
        ('burguers', 'Burguers'),
        ('mexican', 'Mexican'),
        ('drinks', 'Drinks'))

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=255, choices=RESTAURANT_CHOICES, null=True)
    rank = models.IntegerField(default=0)
    profile = models.ForeignKey('Profile',
                                related_name="restaurants", null=True)

    class Meta:
        verbose_name_plural = "restaurants"
