# Generated by Django 3.0.7 on 2020-07-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filiado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_extracao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data da extração')),
                ('hora_da_extracao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Hora da extração')),
                ('numero_da_incricao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numero da inscrição')),
                ('nome_do_filiado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do filiado')),
                ('sigla_do_partido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sigla do partido')),
                ('nome_do_partido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do partido')),
                ('uf', models.CharField(blank=True, max_length=50, null=True, verbose_name='Unidade da federação')),
                ('codigo_do_municipio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Código do município')),
                ('nome_do_municipio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do município')),
                ('zona_eleitoral', models.CharField(blank=True, max_length=50, null=True, verbose_name='Zona eleitoral')),
                ('secao_eleitoral', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seção eleitoral')),
                ('data_da_filiacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data da filiação')),
                ('situacao_do_registro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Situação do registro')),
                ('tipo_do_registro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo do registro')),
                ('data_do_processamento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data do processamento')),
                ('data_da_desfiliacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data da desfiliação')),
                ('data_do_cancelamento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data do cancelamento')),
                ('data_da_regularizacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data da regularização')),
                ('motivo_do_cancelamento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Motivo do cancelamento')),
            ],
            options={
                'ordering': ('nome_do_filiado',),
            },
        ),
    ]
