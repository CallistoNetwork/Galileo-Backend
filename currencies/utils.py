from django.db import connection

from .models import Currency


def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(":")[0].lower()


def tenant_schema_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)


def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")


def get_tenants_map():
    currencies = Currency.objects.all()
    data = {
        f'{currency.name}.localhost': f'{currency.name}'
        for currency in currencies
    }
    return data
