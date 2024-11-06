from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField()
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)
