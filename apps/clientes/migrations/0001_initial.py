# Generated by Django 2.2.1 on 2019-08-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('idactividad', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
                ('secretaria', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaalta', models.DateTimeField(blank=True, null=True)),
                ('datospc', models.CharField(blank=True, max_length=60, null=True)),
                ('idopera', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'db_table': 'actividades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Califica',
            fields=[
                ('idcalifica', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'califica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Canales',
            fields=[
                ('idcanales', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Canal',
                'verbose_name_plural': 'Canales',
                'db_table': 'canales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idcliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=60, null=True)),
                ('fantasia', models.CharField(blank=True, max_length=60, null=True)),
                ('direc_d', models.CharField(blank=True, max_length=60, null=True)),
                ('directivos', models.CharField(blank=True, max_length=60, null=True)),
                ('telef_d', models.CharField(blank=True, max_length=20, null=True)),
                ('email_d', models.CharField(blank=True, max_length=90, null=True)),
                ('localidad', models.CharField(blank=True, max_length=60, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estadocliente',
            fields=[
                ('idestadocliente', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=40, null=True)),
                ('fechaalta', models.DateTimeField(blank=True, null=True)),
                ('datospc', models.CharField(blank=True, max_length=60, null=True)),
                ('idopera', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'estadocliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('idprovincias', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=40, null=True)),
                ('dgi', models.IntegerField(blank=True, null=True)),
                ('declara', models.CharField(blank=True, max_length=1, null=True)),
                ('fechaalta', models.DateTimeField(blank=True, null=True)),
                ('datospc', models.CharField(blank=True, max_length=60, null=True)),
                ('idopera', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('idzona', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=60, null=True)),
                ('fechaalta', models.DateTimeField(blank=True, null=True)),
                ('datospc', models.CharField(blank=True, max_length=60, null=True)),
                ('idopera', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'db_table': 'zonas',
                'managed': False,
            },
        ),
    ]
