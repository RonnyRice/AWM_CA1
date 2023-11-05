from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return str(self.lon), str(self.lat)