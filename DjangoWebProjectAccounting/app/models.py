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
    taxClosingMonth = models.IntegerField(int)

class Levels (models.Model):
    id=models.IntegerField(int)
    description=models.CharField()


class AccountingAccounts (models.Model):
    id = models.CharField()
    description = models.CharField()
    accountType = models.ForeignKey(AccountTypes)
    allowsTransactions = models.BooleanField(bool)
    level = models.ForeignKey(Levels) # 1 to 3
    majorAccount = models.CharField()
    balance = models.FloatField(float)
    state = models.FloatField(float)


class AccountTypes (models.Model):
    id = models.CharField()
    description = models.CharField()
    origin = models.CharField() # DB to CR
    state = models.BooleanField(bool)

class CurrencyTypes (models.Model):
    id = models.CharField()
    description = models.CharField()
    lastExchangeRate = models.FloatField(float)
    state = models.BooleanField(bool)

#class AccountingEntry(models.Model):






