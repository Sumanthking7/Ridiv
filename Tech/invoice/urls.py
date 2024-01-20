from django.urls import path
from .views import InvoiceListCreateView, InvoiceDetailView, InvoiceDetailListCreateView, InvoiceDetailDetailView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice_details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list-create'),
    path('invoice_details/<int:pk>/', InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]
