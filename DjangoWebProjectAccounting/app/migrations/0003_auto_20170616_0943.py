# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170613_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingaccounts',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='accountingaccounts',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], verbose_name='Nivel'),
        ),
        migrations.AlterField(
            model_name='accountingaccounts',
            name='majorAccount',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='app.AccountingAccounts', verbose_name='Cuenta Major'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='taxClosingMonth',
            field=models.IntegerField(verbose_name='Mes Cierre Fiscal'),
        ),
    ]
