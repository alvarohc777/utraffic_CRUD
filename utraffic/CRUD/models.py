from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre


class Factura(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    comentarios = models.TextField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.id_cliente}"

    def save(self, *args, **kwargs):
        if not self.id:
            # Si es una nueva instancia, establece el saldo igual al valor
            self.saldo = self.valor
        super().save(*args, **kwargs)


class PagoFactura(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    comentarios = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id_factura} - {self.fecha}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.id_factura.saldo -= self.valor
        self.id_factura.save(update_fields=["saldo"])
        # self.id_factura.save
