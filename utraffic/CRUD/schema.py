from datetime import date
from typing import List
from ninja import Schema, ModelSchema, Field
from ninja.orm import create_schema
from CRUD.models import Cliente, Factura, PagoFactura

# Clientes
ClienteBase = create_schema(Cliente, fields=["id", "nombre", "direccion", "telefono"])
ClienteCreate = create_schema(Cliente, fields=["nombre", "direccion", "telefono"])


# Facturas
class FacturaBase(ModelSchema):
    cliente: ClienteBase
    # cliente: str

    class Config:
        model = Factura
        model_fields = [
            "id",
            "cliente",
            "fecha",
            "valor",
            "comentarios",
            "saldo",
        ]

    # @staticmethod
    # def resolve_cliente(obj):
    #     return obj.cliente.nombre


FacturaCreate = create_schema(
    Factura, fields=["cliente", "fecha", "valor", "comentarios", "saldo"]
)


#  Pago Facturas
class PagoFacturaBase(ModelSchema):
    factura: FacturaBase

    class Config:
        model = PagoFactura
        model_fields = ["id", "factura", "fecha", "valor", "comentarios"]


PagoFacturaCreate = create_schema(
    PagoFactura, fields=["factura", "fecha", "valor", "comentarios"]
)


class NotFoundSchema(Schema):
    message: str
