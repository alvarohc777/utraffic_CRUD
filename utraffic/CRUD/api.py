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


@api.post("/cliente", response={201: ClienteCreate}, tags=["Cliente"])
# @api.post("/cliente", response={201: ClienteSchemaCreate}, tags=["Cliente"])
def create_cliente(request, cliente: ClienteCreate):
    cliente = Cliente.objects.create(**cliente.dict())
    return cliente


@api.put(
    "/cliente/{cliente_id}",
    response={200: ClienteCreate, 404: NotFoundSchema},
    tags=["Cliente"],
)
def change_cliente(request, cliente_id: int, data: ClienteCreate):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        for attribute, value in data.dict().items():
            setattr(cliente, attribute, value)
        cliente.save()
        return 200, cliente
    except Cliente.DoesNotExist as e:
        return 404, {"message": "El cliente no existe"}


@api.delete(
    "/cliente/{cliente_id}",
    response={200: None, 404: NotFoundSchema},
    tags=["Cliente"],
)
def delete_cliente(request, cliente_id: int):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        cliente.delete()
        return 200
    except Cliente.DoesNotExist as e:
        return 404, {"message": "El cliente no existe"}


# Factura


@api.get("/factura", response=List[FacturaBase], tags=["Factura"])
def facturas(request):
    return Factura.objects.all()


@api.get(
    "/factura/{factura_id}",
    response={200: FacturaBase, 404: NotFoundSchema},
    tags=["Factura"],
)
def factura(request, factura_id: int):
    try:
        factura = Factura.objects.get(pk=factura_id)
        return 200, factura
    except Factura.DoesNotExist as e:
        return 404, {"message": "La factura no existe"}


@api.post("/factura", response={201: FacturaCreate}, tags=["Factura"])
def create_factura(request, factura: FacturaCreate):
    cliente_id = factura.cliente
    cliente = Cliente.objects.get(pk=cliente_id)
    factura = Factura.objects.create(
        cliente=cliente, **factura.dict(exclude={"cliente"})
    )
    return factura


@api.put(
    "/factura/{factura_id}",
    response={200: FacturaBase, 404: NotFoundSchema},
    tags=["Factura"],
)
def change_factura(request, factura_id: int, data: FacturaCreate):
    try:
        factura = Factura.objects.get(pk=factura_id)
        for attribute, value in data.dict().items():
            if attribute == "cliente":
                value = Cliente.objects.get(pk=value)
            setattr(factura, attribute, value)
        factura.save()
        return 200, factura
    except Cliente.DoesNotExist as e:
        return 404, {"message": "La factura no existe"}


@api.delete(
    "/factura/{factura_id}",
    response={200: None, 404: NotFoundSchema},
    tags=["Factura"],
)
def delete_factura(request, factura_id: int):
    try:
        factura = Factura.objects.get(pk=factura_id)
        factura.delete()
        return 200
    except factura.DoesNotExist as e:
        return 404, {"message": "El factura no existe"}


# PagoFactura


@api.get("/pago", response=List[PagoFacturaBase], tags=["Pago Factura"])
def pagos(request):
    return PagoFactura.objects.all()


@api.get(
    "/pago/{pago_id}",
    response={200: PagoFacturaBase, 404: NotFoundSchema},
    tags=["Pago Factura"],
)
def pago(request, pago_id: int):
    try:
        pago = PagoFactura.objects.get(pk=pago_id)
        return 200, pago
    except Factura.DoesNotExist as e:
        return 404, {"message": "La factura no existe"}


@api.post("/pago", response={201: PagoFacturaCreate}, tags=["Pago Factura"])
def create_pago(request, pago: PagoFacturaCreate):
    factura_id = pago.factura
    factura = Factura.objects.get(pk=factura_id)
    pago = PagoFactura.objects.create(factura=factura, **pago.dict(exclude={"factura"}))
    return pago


@api.put(
    "/pago/{pago_id}",
    response={200: PagoFacturaBase, 404: NotFoundSchema},
    tags=["Pago Factura"],
)
def change_pago(request, pago_id: int, data: PagoFacturaCreate):
    try:
        pago = PagoFactura.objects.get(pk=pago_id)
        for attribute, value in data.dict().items():
            if attribute == "factura":
                value = Factura.objects.get(pk=value)
            setattr(pago, attribute, value)
        pago.save()
        return 200, pago
    except Cliente.DoesNotExist as e:
        return 404, {"message": "No se registra pago."}


@api.delete(
    "/pago/{pago_id}",
    response={200: None, 404: NotFoundSchema},
    tags=["Pago Factura"],
)
def delete_pago(request, pago_id: int):
    try:
        pago = PagoFactura.objects.get(pk=pago_id)
        pago.delete()
        return 200
    except factura.DoesNotExist as e:
        return 404, {"message": "No existe el pago."}
