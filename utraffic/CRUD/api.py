from ninja import NinjaAPI
from typing import List, Optional

from CRUD.models import Cliente, Factura, PagoFactura
from CRUD.schema import (
    ClienteBase,
    ClienteCreate,
    FacturaBase,
    FacturaCreate,
    PagoFacturaBase,
    PagoFacturaCreate,
    NotFoundSchema,
)


api = NinjaAPI()


# Cliente


@api.get("/cliente", response=List[ClienteBase], tags=["Cliente"])
def clientes(request, nombre: Optional[str] = None):
    if nombre:
        return Cliente.objects.filter(nombre__icontains=nombre)
    return Cliente.objects.all()


@api.get(
    "/cliente/{cliente_id}",
    response={200: ClienteBase, 404: NotFoundSchema},
    tags=["Cliente"],
)
def cliente(request, cliente_id: int):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        return 200, cliente
    except Cliente.DoesNotExist as e:
        return 404, {"message": "El cliente no existe"}


# def create_cliente(request, payload: ClienteSchema):


@api.get("/hello")
def hello(request):
    return "Hello World"
