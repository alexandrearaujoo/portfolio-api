from django.db import models
import uuid

from users.utils import CustomUserManager


class User(models.Model):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, null=False, unique=True)

    techs = models.ManyToManyField(
        "techs.Tech", on_delete=models.CASCADE, related_name="users"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()
