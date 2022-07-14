from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def __create_user__(self, email, password, name, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            name=name,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password, name, **extra_fields):
        return self.__create_user__(
            email,
            password,
            name,
            False,
            **extra_fields
        )
    
    def create_superuser(self, email, password, name, **extra_fields):
        return self.__create_user__(
            email,
            password,
            name,
            True,
            **extra_fields
        )