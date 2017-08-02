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
    origin = models.CharField('Origen',max_length=3,choices=(('DB','Debito'),('CR','Credito'))) # DB to CR
    state = models.BooleanField('Activo?')
    
    def __str__(self):
         return self.description
    

class AccountingAccounts (models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('Nombre',max_length=20)
    description = models.CharField('Descripción',max_length=30)
    accountTypeId = models.ForeignKey(AccountTypes,on_delete=models.CASCADE,verbose_name='Tipo de Cuenta')
    allowsTransactions = models.BooleanField('Permitir Transacciones?')
    level = models.PositiveSmallIntegerField('Nivel',choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'))) # 1 to 6
    majorAccount = models.ForeignKey('self',default='',verbose_name="Cuenta Major", blank=True, null=True, on_delete=models.CASCADE)
    balance = models.DecimalField('Balance',max_digits=9, decimal_places=2,default=0)
    state = models.BooleanField('Activo?')

    def __str__(self):
         return self.name
    
#class AccountingAccountsAdmin(admin.ModelAdmin):
 #   model = AccountingAccounts
  #  list_display = ['name', 
   #         'description', 
    #        'accountTypeId', 
     #       'allowsTransactions', 
      #      'level', 
       #     'majorAccount',
        #    'balance',
         #   'state', ]


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
    auxiliarOrigin = models.IntegerField('Auxiliar',default = 1)#models.ForeignKey(AuxiliarOrigin) #Identificador del Auxiliar Origen o Propio Módulo Contabilidad
    accountId = models.ForeignKey(AccountingAccounts,on_delete=models.CASCADE)
    movementTypeId = models.ForeignKey(MovementTypes,on_delete=models.CASCADE)
    datetime = models.DateField('Fecha', blank = True)
    amount = models.DecimalField('Monto',max_digits=11, decimal_places=2)
    state = models.BooleanField('Activo?')


class Majorization(models.Model):
    id = models.AutoField('ID', primary_key=True)
    accountId = majorAccountId = models.ForeignKey(AccountingAccounts, related_name='Majorization_accountId',on_delete=models.CASCADE)
    majorAccountId = models.ForeignKey(AccountingAccounts, related_name='Majorization_majorAccountId',on_delete=models.CASCADE)
    movementTypeId = models.ForeignKey(MovementTypes,on_delete=models.CASCADE)
    datetime = models.DateField('Fecha')
    balance = models.DecimalField('Monto',max_digits=5, decimal_places=2)
    state = models.BooleanField('Activo?')