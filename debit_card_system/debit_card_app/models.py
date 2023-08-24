from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

class Cuenta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

class Tarjeta(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


