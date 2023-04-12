from django.contrib import admin
from CRUD.models import Factura, Cliente, PagoFactura

# Register your models here.


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "fecha", "saldo")
    exclude = ("saldo",)
    search_fields = (
        "cliente",
        "fecha",
    )
    list_filter = ("fecha",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "direccion")
    search_fields = ("nombre", "telefono", "direccion")


@admin.register(PagoFactura)
class PagoFactura(admin.ModelAdmin):
    list_display = ("pk", "factura", "fecha", "valor")
    search_fields = ("factura", "fecha", "valor")
    list_filter = ("fecha",)
