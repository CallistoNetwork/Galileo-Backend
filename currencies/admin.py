from django.contrib import admin

from .models import Currency, Domain


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials', 'schema_name')


class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'currency')

    def currency(self, obj):
        return obj.tenant
    currency.short_description = 'Currency'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs.exclude(tenant__schema_name='public')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Domain, DomainAdmin)
