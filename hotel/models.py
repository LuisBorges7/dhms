from django.db import models

class Quarto(models.Model):
    CATEGORIA_QUARTO = (
        ('TUR', 'TURISTA'),
        ('EXE', 'EXECUTIVA'),
        ('PRS', 'PRESIDENCIAL'),
        ('IMP', 'IMPERIAL'),
    )
    
    numero = models.IntegerField()
    categoria = models.CharField(max_length=3, choices=CATEGORIA_QUARTO)
    camas = models.IntegerField()
    capacidade = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.numero}. {self.categoria} com {self.camas} cama(s) para {self.capacidade} pessoa(s)'



