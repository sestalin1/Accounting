"""
Definition of urls for DjangoWebProjectAccounting.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.accountingAccounts, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    
    #accountingAccounts========================================

    url(r'^accountingAccounts/$', app.views.accountingAccounts, name='accountingAccounts'),
    url(r'^accountingAccounts/create/$', app.views.accountingAccountsCreate, name='accountingAccountsCreate'),
    url(r'^accountingAccounts/(?P<pk>\d+)/update/$', app.views.accountingAccountsUpdate, name='accountingAccountsUpdate'),
    url(r'^accountingAccounts/(?P<pk>\d+)/delete/$', app.views.accountingAccountsDelete, name='accountingAccountsDelete'),
    
    #accountTypes========================================

    url(r'^accountTypes/$', app.views.accountTypes, name='accountTypes'),
    url(r'^accountTypes/create/$', app.views.accountTypesCreate, name='accountTypesCreate'),
    url(r'^accountTypes/(?P<pk>\d+)/update/$', app.views.accountTypesUpdate, name='accountTypesUpdate'),
    url(r'^accountTypes/(?P<pk>\d+)/delete/$', app.views.accountTypesDelete, name='accountTypesDelete'),
    
    #levels========================================

    url(r'^levels/$', app.views.levels, name='levels'),
    url(r'^levels/create/$', app.views.levelsCreate, name='levelsCreate'),
    url(r'^levels/(?P<pk>\d+)/update/$', app.views.levelsUpdate, name='levelsUpdate'),
    url(r'^levels/(?P<pk>\d+)/delete/$', app.views.levelsDelete, name='levelsDelete'),
    
    #settings========================================

    url(r'^settings/$', app.views.settings, name='settings'),
    url(r'^settings/create/$', app.views.settingsCreate, name='settingsCreate'),
    url(r'^settings/(?P<pk>\d+)/update/$', app.views.settingsUpdate, name='settingsUpdate'),
    url(r'^settings/(?P<pk>\d+)/delete/$', app.views.settingsDelete, name='settingsDelete'),
    
    #movementTypes========================================

    url(r'^movementTypes/$', app.views.movementTypes, name='movementTypes'),
    url(r'^movementTypes/create/$', app.views.movementTypesCreate, name='movementTypesCreate'),
    url(r'^movementTypes/(?P<pk>\d+)/update/$', app.views.movementTypesUpdate, name='movementTypesUpdate'),
    url(r'^movementTypes/(?P<pk>\d+)/delete/$', app.views.movementTypesDelete, name='movementTypesDelete'),
    
    #currencyTypes========================================

    url(r'^currencyTypes/$', app.views.currencyTypes, name='currencyTypes'),
    url(r'^currencyTypes/create/$', app.views.currencyTypesCreate, name='currencyTypesCreate'),
    url(r'^currencyTypes/(?P<pk>\d+)/update/$', app.views.currencyTypesUpdate, name='currencyTypesUpdate'),
    url(r'^currencyTypes/(?P<pk>\d+)/delete/$', app.views.currencyTypesDelete, name='currencyTypesDelete'),
    
    #auxiliarOrigin========================================

    url(r'^auxiliarOrigin/$', app.views.auxiliarOrigin, name='auxiliarOrigin'),
    url(r'^auxiliarOrigin/create/$', app.views.auxiliarOriginCreate, name='auxiliarOriginCreate'),
    url(r'^auxiliarOrigin/(?P<pk>\d+)/update/$', app.views.auxiliarOriginUpdate, name='auxiliarOriginUpdate'),
    url(r'^auxiliarOrigin/(?P<pk>\d+)/delete/$', app.views.auxiliarOriginDelete, name='auxiliarOriginDelete'),
    
    #accountingEntry========================================

    url(r'^accountingEntry/$', app.views.accountingEntry, name='accountingEntry'),
    url(r'^accountingEntry/create/$', app.views.accountingEntryCreate, name='accountingEntryCreate'),
    url(r'^accountingEntry/(?P<pk>\d+)/update/$', app.views.accountingEntryUpdate, name='accountingEntryUpdate'),
    url(r'^accountingEntry/(?P<pk>\d+)/delete/$', app.views.accountingEntryDelete, name='accountingEntryDelete'),
    
    #majorization========================================

    url(r'^majorization/$', app.views.majorization, name='majorization'),
    url(r'^majorization/create/$', app.views.majorizationCreate, name='majorizationCreate'),
    url(r'^majorization/(?P<pk>\d+)/update/$', app.views.majorizationUpdate, name='majorizationUpdate'),
    url(r'^majorization/(?P<pk>\d+)/delete/$', app.views.majorizationDelete, name='majorizationDelete'),
    
    #===========================================================

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
