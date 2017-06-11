"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Settings(models.Model):
    year = models.IntegerField(int)
    month = models.IntegerField(int)
    majorizationProcessed = models.BooleanField(bool)
    companyRNC = models.IntegerField(int)
    taxClosingMonth = models.DecimalField(max_digits=5, decimal_places=2)

class Levels (models.Model):
    description = models.CharField(max_length=30)

class AccountTypes (models.Model):
    description = models.CharField(max_length=30)
    origin = models.CharField(max_length=2) # DB to CR
    state = models.BooleanField(bool)

class AccountingAccounts (models.Model):
    char = models.CharField('Código',max_length=20)
    description = models.CharField('Descripción',max_length=30)
    accountTypeId = models.ForeignKey(AccountTypes)
    allowsTransactions = models.BooleanField('Permitir Transacciones?')
    level = models.ForeignKey(Levels) # 1 to 3
    majorAccount = models.ForeignKey('self')
    balance = models.DecimalField('Balance',max_digits=5, decimal_places=2)
    state = models.BooleanField('Estado')


class MovementTypes (models.Model):
    label = models.CharField(max_length=20)
    description = models.CharField(max_length=30)



class CurrencyTypes (models.Model):
    lavelId = models.CharField(max_length=5)
    description = models.CharField(max_length=20)
    lastExchangeRate =models.DecimalField(max_digits=5, decimal_places=2)
    state = models.BooleanField(bool)

class AuxiliarOrigin(models.Model):
    description = models.CharField(max_length=30)

class AccountingEntry(models.Model):
    seatId = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    auxiliarOriginId = models.ForeignKey(AuxiliarOrigin) #Identificador del Auxiliar Origen o Propio Módulo Contabilidad
    accountId = models.ForeignKey(AccountingAccounts)
    movementTypeId = models.ForeignKey(MovementTypes)
    datetime = models.DateField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.BooleanField(bool)


class Majorization(models.Model):
    accountId = models.CharField(max_length=30)
    majorAccountId = models.ForeignKey(AccountingAccounts)
    movementTypeId = models.ForeignKey(MovementTypes)
    datetime = models.DateField()
    balance = models.DecimalField(max_digits=5, decimal_places=2)
    state = models.BooleanField(bool)