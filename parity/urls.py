from django.urls import path

from .views import (
    SaveView, GetBlockInfoView, GetTransactionInfoView, GetAddressInfoView
)

urlpatterns = [
    path(
        '',
        SaveView.as_view(),
        name='save'
    ),
    path(
        'block-info/<str:hash>/',
        GetBlockInfoView.as_view(),
        name='get_block_info'
    ),
    path(
        'transaction-info/<str:hash>/',
        GetTransactionInfoView.as_view(),
        name='get_transaction_info'
    ),
    path(
        'address-info/<str:hash>/',
        GetAddressInfoView.as_view(),
        name='get_address_info'
    )
]
