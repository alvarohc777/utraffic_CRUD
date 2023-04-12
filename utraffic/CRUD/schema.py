from datetime import date
from ninja import Schema


class ClienteSchema(Schema):
    id: int
    nombre: str
    direccion: str
    telefono: str


class FacturaSchema(Schema):
    id_cliente: int
    fecha: date
    valor: float
    comentarios: str
    saldo: float


class PagoFacturaSchema(Schema):
    id_factura: int
    fecha: date
    valor: float
    comentarios: str


class NotFoundSchema(Schema):
    message: str
