# Generated by Django 3.1.7 on 2021-04-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguranca_trabalho', '0003_auto_20210412_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='empresa_selecionada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='seguranca_trabalho.empresa'),
        ),
    ]