from django.db import models

from mailauth.models import CustomUser


class Point(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    record = models.IntegerField(default=0)
