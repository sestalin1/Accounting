"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import *




class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AccountingAccountsForm(forms.ModelForm):
    
    class Meta:
        model = AccountingAccounts
         
        fields = (
            #'id', 
            'name', 
            'description', 
            'accountTypeId', 
            'allowsTransactions', 
            'level', 
            'majorAccount',
            'balance',
            'state',
           
 )
        #accountTypeId = CustomModelChoiceField(queryset=AccountTypes.objects.all())

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = (
            'id', 
            'year', 
            'month', 
            'majorizationProcessed', 
            'companyRNC', 
            'taxClosingMonth', 
           )
        
class LevelsForm(forms.ModelForm):
    class Meta:
        model = Levels
        fields = (
            'id',
            'description', 
           )

class AccountTypesForm(forms.ModelForm):
    class Meta:
        model = AccountTypes
        fields = (
            'id', 
            'description', 
            'origin',
            'state',
           )

class MovementTypesForm(forms.ModelForm):
    class Meta:
        model = MovementTypes
        fields = (
            
            'description', 
           )

class CurrencyTypesForm(forms.ModelForm):
    class Meta:
        model = CurrencyTypes
        fields = (
            'iso', 
            'code', 
            'symbol', 
            'description', 
            'lastExchangeRate',
            'state',
           )
        
class AuxiliarOriginForm(forms.ModelForm):
    class Meta:
        model = AuxiliarOrigin
        fields = (
            'id', 
            'description', 
           )
        
class AccountingEntryForm(forms.ModelForm):
    class Meta:
        model = AccountingEntry
        fields = (
            'id', 
            'description', 
            'auxiliarOriginId', 
            'accountId', 
            'movementTypeId', 
            'datetime',
            'amount',
            'state',
           )
        
class MajorizationForm(forms.ModelForm):
    class Meta:
        model = Majorization
        fields = (
            'id', 
            'accountId', 
            'majorAccountId', 
            'movementTypeId', 
            'datetime', 
            'balance',
            'state',
           )

