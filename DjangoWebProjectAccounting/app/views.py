"""
Definition of views.
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

#accountingAccounts========================================

@login_required
def accountingAccounts(request):
   #if not request.user.is_authenticated:
   #     return redirect(settings.LOGIN_URL, request.path)
  # else:
        accounts = AccountingAccounts.objects.all()
        return render(
        request ,
        'app/accountingAccounts.html' ,
        {
            'title':'Cuentas Contables',
            'accounts': accounts,
            'year':datetime.now().year,
         }
   )

@login_required
def save_account_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            accounts = AccountingAccountsForm.objects.all()
            data['html_account_list'] = render_to_string('app/accountingAccountsPartial.html', {
                'accounts': accounts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def accountingAccountsCreate(request):
    if request.method == 'POST':
        form = AccountingAccountsForm(request.POST)
    else:
        form = AccountingAccountsForm()
    return save_account_form(request, form, 'app/accountingAccountsCreatePartial.html')

@login_required
def accountingAccountsUpdate(request, pk):
    account = get_object_or_404(AccountingAccounts, pk=pk)
    if request.method == 'POST':
        form = AccountingAccountsForm(request.POST, instance=account)
    else:
        form = AccountingAccountsForm(instance=account)
    return save_account_form(request, form, 'app/accountingAccountsUpdatePartial.html')

@login_required
def accountingAccountsDelete(request, pk):
    account = get_object_or_404(AccountingAccounts, pk=pk)
    data = dict()
    if request.method == 'POST':
        account.delete()
        data['form_is_valid'] = True
        accounts = AccountingAccounts.objects.all()
        data['html_account_list'] = render_to_string('app/accountingAccountsPartial.html', {
            'accounts': accounts
        })
    else:
        context = {'account': account}
        data['html_form'] = render_to_string('app/accountingAccountsDeletePartial.html', context, request=request)
    return JsonResponse(data)

#settings========================================

@login_required
def settings(request):
 
        settings = Settings.objects.all()
        return render(
        request ,
        'app/settings.html' ,
        {
            'title':'Configuraciones',
            'settings': settings,
            'year':datetime.now().year,
         }
   )

@login_required
def save_settings_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            settings = Settings.objects.all()
            data['html_settings_list'] = render_to_string('app/settingsPartial.html', {
                'settings': settings
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def settingsCreate(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
    else:
        form = SettingsForm()
    return save_settings_form(request, form, 'app/settingsCreatePartial.html')

@login_required
def settingsUpdate(request, pk):
    settings = get_object_or_404(Settings, pk=pk)
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=settings)
    else:
        form = SettingsForm(instance=settings)
    return save_settings_form(request, form, 'app/settingsUpdatePartial.html')

@login_required
def settingsDelete(request, pk):
    settings = get_object_or_404(Settings, pk=pk)
    data = dict()
    if request.method == 'POST':
        settings.delete()
        data['form_is_valid'] = True
        settings = Settings.objects.all()
        data['html_account_list'] = render_to_string('app/settingsPartial.html', {
            'settings': settings
        })
    else:
        context = {'settings': settings}
        data['html_form'] = render_to_string('app/settingsDeletePartial.html', context, request=request)
    return JsonResponse(data)

#levels========================================

@login_required
def levels(request):
  
        levels = Levels.objects.all()
        return render(
        request ,
        'app/levels.html' ,
        {
            'title':'Niveles',
            'levels': levels,
            'year':datetime.now().year,
         }
   )

@login_required
def save_levels_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            levels = Levels.objects.all()
            data['html_levels_list'] = render_to_string('app/levelsPartial.html', {
                'levels': levels
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def levelsCreate(request):
    if request.method == 'POST':
        form = LevelsForm(request.POST)
    else:
        form = LevelsForm()
    return save_levels_form(request, form, 'app/levelsCreatePartial.html')

@login_required
def levelsUpdate(request, pk):
    levels = get_object_or_404(Levels, pk=pk)
    if request.method == 'POST':
        form = LevelsForm(request.POST, instance=levels)
    else:
        form = LevelsForm(instance=levels)
    return save_levels_form(request, form, 'app/levelsUpdatePartial.html')

@login_required
def levelsDelete(request, pk):
    levels = get_object_or_404(Levels, pk=pk)
    data = dict()
    if request.method == 'POST':
        levels.delete()
        data['form_is_valid'] = True
        levels = Levels.objects.all()
        data['html_levels_list'] = render_to_string('app/levelsPartial.html', {
            'levels': levels
        })
    else:
        context = {'levels': levels}
        data['html_form'] = render_to_string('app/levelsDeletePartial.html', context, request=request)
    return JsonResponse(data)

#accountTypes========================================

@login_required
def accountTypes(request):
 
        accountTypes = AccountTypes.objects.all()
        return render(
        request ,
        'app/AccountTypes.html' ,
        {
            'title':'Tipos de Cuenta',
            'accountTypes': accountTypes,
            'year':datetime.now().year,
         }
   )

@login_required
def save_accountTypes_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            accountTypes = AccountTypes.objects.all()
            data['html_accountTypes_list'] = render_to_string('app/accountTypesPartial.html', {
                'accountTypes': accountTypes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def accountTypesCreate(request):
    if request.method == 'POST':
        form = AccountTypesForm(request.POST)
    else:
        form = AccountTypesForm()
    return save_accountTypes_form(request, form, 'app/accountTypesCreatePartial.html')

@login_required
def accountTypesUpdate(request, pk):
    accountTypes = get_object_or_404(AccountTypes, pk=pk)
    if request.method == 'POST':
        form = AccountTypesForm(request.POST, instance=accountTypes)
    else:
        form = AccountTypesForm(instance=accountTypes)
    return save_accountTypes_form(request, form, 'app/accountTypes.html')

@login_required
def accountTypesDelete(request, pk):
    accountTypes = get_object_or_404(AccountTypes, pk=pk)
    data = dict()
    if request.method == 'POST':
        accountTypes.delete()
        data['form_is_valid'] = True
        accountTypes = AccountTypes.objects.all()
        data['html_accountTypes_list'] = render_to_string('app/accountTypesPartial.html', {
            'accountTypes': accountTypes
        })
    else:
        context = {'accountTypes': accountTypes}
        data['html_form'] = render_to_string('app/accountTypesDeletePartial.html', context, request=request)
    return JsonResponse(data)

#movementTypes========================================

@login_required
def movementTypes(request):
  
        movementTypes = MovementTypes.objects.all()
        return render(
        request ,
        'app/movementTypes.html' ,
        {
            'title':'Tipos de Movimientos',
            'movementTypes': movementTypes,
            'year':datetime.now().year,
         }
   )

@login_required
def save_movementTypes_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            movementTypes = MovementTypes.objects.all()
            data['html_movementTypes_list'] = render_to_string('app/movementTypesPartial.html', {
                'movementTypes': movementTypes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def movementTypesCreate(request):
    if request.method == 'POST':
        form = MovementTypesForm(request.POST)
    else:
        form = MovementTypesForm()
    return save_movementTypes_form(request, form, 'app/movementTypesCreatePartial.html')

@login_required
def movementTypesUpdate(request, pk):
    account = get_object_or_404(MovementTypes, pk=pk)
    if request.method == 'POST':
        form = MovementTypesForm(request.POST, instance=movementTypes)
    else:
        form = MovementTypesForm(instance=movementTypes)
    return save_movementTypes_form(request, form, 'app/movementTypesUpdatePartial.html')

@login_required
def movementTypesDelete(request, pk):
    movementTypes = get_object_or_404(MovementTypes, pk=pk)
    data = dict()
    if request.method == 'POST':
        movementTypes.delete()
        data['form_is_valid'] = True
        movementTypes = MovementTypes.objects.all()
        data['html_movementTypes_list'] = render_to_string('app/movementTypesPartial.html', {
            'movementTypes': movementTypes
        })
    else:
        context = {'movementTypes': movementTypes}
        data['html_form'] = render_to_string('app/movementTypesDeletePartial.html', context, request=request)
    return JsonResponse(data)

#currencyTypes========================================
@login_required
def currencyTypes(request):
 
        currencyTypes = CurrencyTypes.objects.all()
        return render(
        request ,
        'app/currencyTypes.html' ,
        {
            'title':'Tipos de Moneda',
            'currencyTypes': currencyTypes,
            'year':datetime.now().year,
         }
   )

@login_required
def save_currencyTypes_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            currencyTypes = CurrencyTypes.objects.all()
            data['html_currencyTypes_list'] = render_to_string('app/currencyTypes.html', {
                'currencyTypes': currencyTypes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def currencyTypesCreate(request):
    if request.method == 'POST':
        form = CurrencyTypesForm(request.POST)
    else:
        form = CurrencyTypesForm()
    return save_currencyTypes_form(request, form, 'app/currencyTypesCreatePartial.html')

@login_required
def currencyTypesUpdate(request, pk):
    currencyTypes = get_object_or_404(CurrencyTypes, pk=pk)
    if request.method == 'POST':
        form = CurrencyTypesForm(request.POST, instance=currencyTypes)
    else:
        form = CurrencyTypesForm(instance=currencyTypes)
    return save_currencyTypes_form(request, form, 'app/currencyTypesUpdatePartial.html')

@login_required
def currencyTypesDelete(request, pk):
    currencyTypes = get_object_or_404(CurrencyTypes, pk=pk)
    data = dict()
    if request.method == 'POST':
        currencyTypes.delete()
        data['form_is_valid'] = True
        currencyTypes = CurrencyTypes.objects.all()
        data['html_currencyTypes_list'] = render_to_string('app/currencyTypesPartial.html', {
            'currencyTypes': currencyTypes
        })
    else:
        context = {'currencyTypes': currencyTypes}
        data['html_form'] = render_to_string('app/currencyTypesDeletePartial.html', context, request=request)
    return JsonResponse(data)

#auxiliarOrigin========================================
@login_required
def auxiliarOrigin(request):
 
        auxiliarOrigin = AuxiliarOrigin.objects.all()
        return render(
        request ,
        'app/auxiliarOrigin.html' ,
        {
            'title':'Origen Auxiliar',
            'auxiliarOrigin': auxiliarOrigin,
            'year':datetime.now().year,
         }
   )

@login_required
def save_auxiliarOrigin_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            auxiliarOrigin = AuxiliarOriginForm.objects.all()
            data['html_auxiliarOrigin_list'] = render_to_string('app/auxiliarOriginPartial.html', {
                'auxiliarOrigin': auxiliarOrigin
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def auxiliarOriginCreate(request):
    if request.method == 'POST':
        form = AuxiliarOriginForm(request.POST)
    else:
        form = AuxiliarOriginForm()
    return save_auxiliarOrigin_form(request, form, 'app/auxiliarOriginCreatePartial.html')

@login_required
def auxiliarOriginUpdate(request, pk):
    auxiliarOrigin = get_object_or_404(AuxiliarOrigin, pk=pk)
    if request.method == 'POST':
        form = AuxiliarOriginForm(request.POST, instance=auxiliarOrigin)
    else:
        form = AuxiliarOriginForm(instance=auxiliarOrigin)
    return save_auxiliarOrigin_form(request, form, 'app/auxiliarOriginUpdatePartial.html')

@login_required
def auxiliarOriginDelete(request, pk):
    auxiliarOrigin = get_object_or_404(AuxiliarOrigin, pk=pk)
    data = dict()
    if request.method == 'POST':
        auxiliarOrigin.delete()
        data['form_is_valid'] = True
        auxiliarOrigin = AuxiliarOrigin.objects.all()
        data['html_auxiliarOrigin_list'] = render_to_string('app/auxiliarOriginPartial.html', {
            'auxiliarOrigin': auxiliarOrigin
        })
    else:
        context = {'auxiliarOrigin': auxiliarOrigin}
        data['html_form'] = render_to_string('app/auxiliarOriginDeletePartial.html', context, request=request)
    return JsonResponse(data)

#accountingEntry========================================

@login_required
def accountingEntry(request):

        accountingEntry = AccountingEntry.objects.all()
        return render(
        request ,
        'app/accountingEntry.html' ,
        {
            'title':'Entradas Contables',
            'accountingEntry': accountingEntry,
            'year':datetime.now().year,
         }
   )

@login_required
def save_accountingEntry_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            accountingEntry = AccountingEntry.objects.all()
            data['html_accountingEntry_list'] = render_to_string('app/accountingEntryPartial.html', {
                'accountingEntry': accountingEntry
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def accountingEntryCreate(request):
    if request.method == 'POST':
        form = AccountingEntryForm(request.POST)
    else:
        form = AccountingEntryForm()
    return save_accountingEntry_form(request, form, 'app/accountingEntryCreatePartial.html')

@login_required
def accountingEntryUpdate(request, pk):
    accountingEntry = get_object_or_404(AccountingEntry, pk=pk)
    if request.method == 'POST':
        form = AccountingEntryForm(request.POST, instance=accountingEntry)
    else:
        form = AccountingEntryForm(instance=accountingEntry)
    return save_accountingEntry_form(request, form, 'app/accountingEntryUpdatePartial.html')

@login_required
def accountingEntryDelete(request, pk):
    accountingEntry = get_object_or_404(AccountingEntry, pk=pk)
    data = dict()
    if request.method == 'POST':
        accountingEntry.delete()
        data['form_is_valid'] = True
        accountingEntry = AccountingEntry.objects.all()
        data['html_accountingEntry_list'] = render_to_string('app/accountingEntryPartial.html', {
            'accountingEntry': accountingEntry
        })
    else:
        context = {'accountingEntry': accountingEntry}
        data['html_form'] = render_to_string('app/accountingEntryDeletePartial.html', context, request=request)
    return JsonResponse(data)

#majorization========================================
@login_required
def majorization(request):
 
        majorization = Majorization.objects.all()
        return render(
        request ,
        'app/majorization.html' ,
        {
            'title':'Mayorización',
            'majorization': majorization,
            'year':datetime.now().year,
         }
   )

@login_required
def save_majorization_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            majorization = MajorizationForm.objects.all()
            data['html_majorization_list'] = render_to_string('app/majorizationPartial.html', {
                'majorization': majorization
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def majorizationCreate(request):
    if request.method == 'POST':
        form = MajorizationForm(request.POST)
    else:
        form = MajorizationForm()
    return save_majorization_form(request, form, 'app/majorizationCreatePartial.html')

@login_required
def majorizationUpdate(request, pk):
    majorization = get_object_or_404(Majorization, pk=pk)
    if request.method == 'POST':
        form = MajorizationForm(request.POST, instance=majorization)
    else:
        form = MajorizationForm(instance=majorization)
    return save_majorization_form(request, form, 'app/majorizationUpdatePartial.html')

@login_required
def majorizationDelete(request, pk):
    majorization = get_object_or_404(Majorization, pk=pk)
    data = dict()
    if request.method == 'POST':
        majorization.delete()
        data['form_is_valid'] = True
        majorization = Majorization.objects.all()
        data['html_majorization_list'] = render_to_string('app/majorizationPartial.html', {
            'majorization': majorization
        })
    else:
        context = {'majorization': majorization}
        data['html_form'] = render_to_string('app/majorizationDeletePartial.html', context, request=request)
    return JsonResponse(data)

#==============================================================