from django.db import models

# Create your models here.

class Moneda(models.Model):
    Nombre = models.CharField(max_length=10)
    Simbolo = models.CharField(max_length=3)

class BancoLibrador(models.Model):
    Nombre = models.CharField(max_length=30)


class ChEmitidos(models.Model):

    FechaEmision = models.DateField()
    FechaPago = models.DateField()
    Serie = models.IntegerField()
    Numero = models.IntegerField()
    Proveedor = models.CharField(max_length=60)
    BancoLibrador = models.ForeignKey(BancoLibrador, on_delete=models.CASCADE)
    Moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

class ChRecibidos(models.Model):

    fechaEmision = models.DateField()
    fechaCobro = models.DateField()
    serie = models.IntegerField()
    numero = models.IntegerField()
    cliente = models.CharField(max_length=60)
    bancoLibrador = models.ForeignKey(BancoLibrador, on_delete=models.CASCADE)
    Moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    

