from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Currency(TenantMixin):
    name = models.CharField(
        max_length=255
    )
    initials = models.CharField(
        max_length=50
    )

    def __str__(self):
        return f'{self.name} ({self.initials})'


class Domain(DomainMixin):
    pass
