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
    account = get_object_or_404(accountingAccounts, pk=pk)
    if request.method == 'POST':
        form = AccountingAccountsForm(request.POST, instance=account)
    else:
        form = AccountingAccountsForm(instance=account)
    return save_account_form(request, form, 'app/accountingAccountsUpdatePartial.html')

@login_required
def accountingAccountsDelete(request, pk):
    account = get_object_or_404(accountingAccounts, pk=pk)
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