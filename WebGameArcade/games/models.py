from django.db import models

from mailauth.models import CustomUser


class Point(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    record = models.IntegerField(default=0)