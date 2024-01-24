from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name