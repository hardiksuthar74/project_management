from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    profile_file = models.FileField(upload_to="files/user_profile", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["username"]

    def __str__(self):
        return self.username
