from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

from users.utils import CustomUserManager


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, null=False, unique=True)

    techs = models.ManyToManyField(
        "techs.Tech", related_name="users"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

