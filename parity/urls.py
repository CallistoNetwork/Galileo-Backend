from django.urls import path

from .views import SaveView

urlpatterns = [
    path('', SaveView.as_view(), name='save'),
]
