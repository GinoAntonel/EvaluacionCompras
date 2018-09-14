# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Compras(models.Model):
    texto = models.CharField('Texto', max_length=50, null=False, blank=False)
    fecha = models.DateTimeField('Fecha', auto_now=True)
    archived = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Compra: {}'.format(self.texto)