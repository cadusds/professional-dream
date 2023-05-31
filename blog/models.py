from django.conf import settings
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    bio = models.CharField(max_length=250,blank=True)

    def __str__(self) -> str:
        return self.user.get_username()