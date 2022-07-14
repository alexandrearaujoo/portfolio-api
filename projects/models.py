import uuid
from django.db import models

def upload_img_project(instance, filename):
    return f'{instance.id}-{filename}'


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=126, null=False)
    type = models.CharField(max_length=126, null=False)
    slug = (models.CharField(max_length=126, null=True),)
    img = models.ImageField(upload_to=upload_img_project, null=True, blank=True)
    link_website = models.CharField(max_length=126, null=False)
    link_repository = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=256, null=True)

    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="projects"
    )
