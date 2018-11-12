from django.contrib import admin

from .models import Currency, Domain


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'initials', 'schema_name')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Domain)
