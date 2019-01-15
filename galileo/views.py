from django.http import JsonResponse
from django.views import View

from currencies.models import Domain


class HomeView(View):
    def get(self, request, *args, **kwargs):
        domains = Domain.objects.all()

        data = [
            {
                'url': domain.domain,
                'name': domain.tenant.name
            } for domain in domains
        ]
        return JsonResponse(data=data, safe=False)
