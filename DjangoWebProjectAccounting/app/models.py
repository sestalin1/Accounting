"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Settings(models.Model):
    id = models.AutoField('ID', primary_key=True)
    year = models.IntegerField('Año')
    month = models.IntegerField('Mes')
    majorizationProcessed = models.BooleanField('Mayorización procesada')
    companyRNC = models.IntegerField('Empresa RNC')
    taxClosingMonth = models.IntegerField('Mes Cierre Fiscal')

class Levels (models.Model):
    id = models.AutoField('ID', primary_key=True,default=1)
    description = models.CharField(max_length=30)

class AccountTypes (models.Model):
    id = models.AutoField('ID', primary_key=True)
    description = models.CharField('Descripción',max_length=30)
    origin = models.CharField('Origen',max_length=2) # DB to CR
    state = models.BooleanField('Activo?')

class AccountingAccounts (models.Model):
    id = models.CharField('ID',max_length=20, primary_key=True)
    description = models.CharField('Descripción',max_length=30)
    accountTypeId = models.ForeignKey(AccountTypes)
    allowsTransactions = models.BooleanField('Permitir Transacciones?')
    level = models.PositiveSmallIntegerField('Nivel',choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'))) # 1 to 6
    majorAccount = models.ForeignKey('self',default='',verbose_name="Cuenta Major", blank=True)
    balance = models.DecimalField('Balance',max_digits=5, decimal_places=2,default=0)
    state = models.BooleanField('Activo?')


class MovementTypes (models.Model):
    id = models.CharField('ID',max_length=20, primary_key=True)
    description = models.CharField('Descripción',max_length=30)


class CurrencyTypes (models.Model):
    iso = models.IntegerField('ISO', primary_key=True, default=0)
    code = models.CharField('Código',max_length=5, default='')
    symbol = models.CharField('Símbolo',max_length=5, default='')
    description = models.CharField('Descripción',max_length=20)
    lastExchangeRate = models.DecimalField('Última Tasa Cambiaria', max_digits=5, decimal_places=2)
    state = models.BooleanField('Activo?')

class AuxiliarOrigin(models.Model):
    id = models.AutoField('ID', primary_key=True)
    description = models.CharField('Descripción',max_length=30)

class AccountingEntry(models.Model):
    id = models.AutoField('ID', primary_key=True)
    description = models.CharField('Descripción',max_length=30)
    auxiliarOriginId = models.ForeignKey(AuxiliarOrigin) #Identificador del Auxiliar Origen o Propio Módulo Contabilidad
    accountId = models.ForeignKey(AccountingAccounts)
    movementTypeId = models.ForeignKey(MovementTypes)
    datetime = models.DateField('Fecha')
    amount = models.DecimalField('Monto',max_digits=5, decimal_places=2)
    state = models.BooleanField('Activo?')


class Majorization(models.Model):
    id = models.AutoField('ID', primary_key=True)
    accountId = majorAccountId = models.ForeignKey(AccountingAccounts, related_name='Majorization_accountId')
    majorAccountId = models.ForeignKey(AccountingAccounts, related_name='Majorization_majorAccountId')
    movementTypeId = models.ForeignKey(MovementTypes)
    datetime = models.DateField('Fecha')
    balance = models.DecimalField('Monto',max_digits=5, decimal_places=2)
    state = models.BooleanField('Activo?')