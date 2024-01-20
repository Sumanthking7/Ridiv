from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from invoice.models import Invoice, InvoiceDetail

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-01-21', 'customer_name': 'Test Customer'}

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)

    def test_get_invoices(self):
        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 0)

    def test_get_single_invoice(self):
        invoice = Invoice.objects.create(date='2024-01-21', customer_name='Test Customer')
        response = self.client.get(f'/invoices/{invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Test Customer')

    def test_update_invoice(self):
        invoice = Invoice.objects.create(date='2024-01-21', customer_name='Test Customer')
        updated_data = {'date': '2024-01-22', 'customer_name': 'Updated Customer'}
        response = self.client.put(f'/invoices/{invoice.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Updated Customer')
        # Optionally, check if the database has been updated
        updated_invoice = Invoice.objects.get(id=invoice.id)
        self.assertEqual(updated_invoice.customer_name, 'Updated Customer')

    def test_delete_invoice(self):
        invoice = Invoice.objects.create(date='2024-01-21', customer_name='Test Customer')
        response = self.client.delete(f'/invoices/{invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)
