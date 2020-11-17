import uuid
from django.contrib.auth.models import AbstractUser


from django.db import models

class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
    user_type = models.CharField(max_length=10, default='', null=True, blank=True)
    user_addr = models.CharField(max_length=200, default='', null=True, blank=True)
    user_city = models.CharField(max_length=100, default='', null=True, blank=True)
    user_state = models.CharField(max_length=2, default='', null=True, blank=True)
    user_zipcode = models.IntegerField(null=True, blank=True)
    user_phone = models.IntegerField(null=True, blank=True)
