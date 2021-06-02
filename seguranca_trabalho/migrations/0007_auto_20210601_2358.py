# Generated by Django 3.1.7 on 2021-06-01 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguranca_trabalho', '0006_auto_20210601_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='seguranca_trabalho.cargo'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='funcao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='seguranca_trabalho.funcao'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='setor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='seguranca_trabalho.setor'),
        ),
    ]
