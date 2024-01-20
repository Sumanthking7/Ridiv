from django.contrib import admin

# Register your models here.

# invoice/admin.py
from django.contrib import admin
from .models import Invoice, InvoiceDetail

class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]

admin.site.register(Invoice, InvoiceAdmin)