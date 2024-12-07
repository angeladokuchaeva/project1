import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Country(models.Model):
    country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VisitedCountry(models.Model):
    visited_country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visited_countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='visitors')


class FavouriteCountry(models.Model):
    favourite_country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_countries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='favourites')


class Impression(models.Model):
    impression_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='impressions')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='impressions')
    description = models.TextField()
