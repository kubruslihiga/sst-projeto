# Generated by Django 3.1.7 on 2021-05-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguranca_trabalho', '0002_auto_20210529_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunicacaoacidentetrabalho',
            name='natureza_lesao_classificao',
        ),
        migrations.AddField(
            model_name='comunicacaoacidentetrabalho',
            name='numero_inscricao_medica',
            field=models.CharField(default='', max_length=20, verbose_name='Número de inscrição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agentecausadoracidentetrabalho',
            name='codigo',
            field=models.CharField(max_length=15, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='agentecausadoracidentetrabalho',
            name='descricao',
            field=models.CharField(max_length=1000, null=True, verbose_name='Descriçao'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='categoria',
            field=models.CharField(max_length=200, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='codigo',
            field=models.CharField(max_length=20, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='descricao',
            field=models.CharField(max_length=2000, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='comunicacaoacidentetrabalho',
            name='acidente_aviso_comunicacao',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (None, None)], verbose_name='Comunicação do acidente'),
        ),
        migrations.AlterField(
            model_name='comunicacaoacidentetrabalho',
            name='classificao_codigo_medico',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (None, None)], verbose_name='Órgão de classe'),
        ),
        migrations.AlterField(
            model_name='comunicacaoacidentetrabalho',
            name='lado_parte_corpo_atingida',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (None, None)], verbose_name='Lado do corpo atingida'),
        ),
        migrations.AlterField(
            model_name='comunicacaoacidentetrabalho',
            name='tipo_cat',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (None, None)], null=True, verbose_name='Tipo da CAT'),
        ),
        migrations.AlterField(
            model_name='comunicacaoacidentetrabalho',
            name='tipo_inscricao',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (4, 4), (None, None)], verbose_name='Tipo de inscrição'),
        ),
        migrations.AlterField(
            model_name='comunicacaoacidentetrabalho',
            name='tipo_localizacao_acidente',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (9, 9), (None, None)], verbose_name='Tipo do local do acidente'),
        ),
        migrations.AlterField(
            model_name='fatoracidente',
            name='codigo',
            field=models.CharField(max_length=10, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='fatoracidente',
            name='descricao',
            field=models.CharField(max_length=500, null=True, verbose_name='Descriçao'),
        ),
        migrations.AlterField(
            model_name='fatorrisco',
            name='categoria',
            field=models.CharField(max_length=200, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='fatorrisco',
            name='codigo',
            field=models.CharField(max_length=20, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='fatorrisco',
            name='descricao',
            field=models.CharField(max_length=2000, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='naturezalesao',
            name='codigo',
            field=models.CharField(max_length=15, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='naturezalesao',
            name='descricao',
            field=models.CharField(max_length=750, null=True, verbose_name='Descriçao'),
        ),
        migrations.AlterField(
            model_name='partecorpoatingida',
            name='codigo',
            field=models.CharField(max_length=15, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='partecorpoatingida',
            name='descricao',
            field=models.CharField(max_length=500, null=True, verbose_name='Descriçao'),
        ),
        migrations.AlterField(
            model_name='tipoacidente',
            name='codigo',
            field=models.CharField(max_length=10, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='tipoacidente',
            name='descricao',
            field=models.CharField(max_length=500, null=True, verbose_name='Descriçao'),
        ),
        migrations.AlterField(
            model_name='unidademedida',
            name='codigo',
            field=models.CharField(max_length=20, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='unidademedida',
            name='descricao',
            field=models.CharField(max_length=2000, verbose_name='Descrição'),
        ),
    ]
