from django.db import models

class User(models.Model):
    username = None
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, null=False)

    techs = models.ManyToManyField('techs.Tech', on_delete=models.CASCADE, related_name='users')
