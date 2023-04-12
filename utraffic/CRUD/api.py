from ninja import NinjaAPI
from typing import List, Optional

from CRUD.models import Cliente, Factura, PagoFactura
from CRUD.schema import ClienteSchema, FacturaSchema, PagoFacturaSchema, NotFoundSchema


api = NinjaAPI()


@api.get("/cliente", response=List[ClienteSchema])
def clientes(request, nombre: Optional[str] = None):
    if nombre:
        return Cliente.objects.filter(nombre__icontains=nombre)
    return Cliente.objects.all()


@api.get("/cliente/{cliente_id}", response={200: ClienteSchema, 404: NotFoundSchema})
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
