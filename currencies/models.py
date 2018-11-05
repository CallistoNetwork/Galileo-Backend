from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=255
    )
    initials = models.CharField(
        max_length=50
    )
    subdomain = models.CharField(
        max_length=50
    )
