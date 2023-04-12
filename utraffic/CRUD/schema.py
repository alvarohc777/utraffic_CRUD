from datetime import date
from ninja import Schema, ModelSchema
from ninja.orm import create_schema
from CRUD.models import Cliente, Factura, PagoFactura


ClienteBase = create_schema(Cliente, fields=["id", "nombre", "direccion", "telefono"])
ClienteCreate = create_schema(Cliente, fields=["nombre", "direccion", "telefono"])

# class ClienteSchema(ModelSchema):
#     class Config:
#         model = Cliente
#         model_fields = ["nombre", "direccion", "telefono"]


# class ClienteSchema(Schema):
#     nombre: str
#     direccion: str
#     telefono: str


# class FacturaBase(ModelSchema):
#     class Config:
#         model = Factura
#         model_fields = ["id", "cliente", "fecha", "valor", "comentarios", "saldo"]


# class FacturaCreate(ModelSchema):
#     class Config:
#         model = Factura
#         model_fields = ["cliente", "fecha", "valor", "comentarios", "saldo"]


FacturaBase = create_schema(
    Factura, fields=["id", "cliente", "fecha", "valor", "comentarios", "saldo"]
)
FacturaCreate = create_schema(
    Factura, fields=["cliente", "fecha", "valor", "comentarios", "saldo"]
)
PagoFacturaBase = create_schema(
    PagoFactura, fields=["id", "factura", "fecha", "valor", "comentarios"]
)
PagoFacturaCreate = create_schema(
    PagoFactura, fields=["factura", "fecha", "valor", "comentarios"]
)


class NotFoundSchema(Schema):
    message: str
