# Generated by Django 3.2 on 2021-08-25 15:49

import apps.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('normas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_surname', models.CharField(blank=True, help_text='Apellido Paterno', max_length=50, verbose_name='Apellido Paterno')),
                ('second_surname', models.CharField(blank=True, help_text='Apellido Materno', max_length=50, verbose_name='Apellido Materno')),
                ('names', models.CharField(help_text='Nombres O Razón Social', max_length=50, verbose_name='Nombres')),
                ('full_name', models.CharField(default='Nombre completo', help_text='Apellidos y Nombres', max_length=200, verbose_name='Apellidos y Nombres')),
                ('person_type', models.CharField(choices=[('N', 'NATURAL'), ('J', 'JURÍDICA')], default='N', help_text='Tipo de Persona', max_length=1, verbose_name='Tipo de Persona')),
                ('identity', models.CharField(blank=True, help_text='DNI o RUC', max_length=11, verbose_name='Documento de Identidad')),
                ('profession', models.CharField(blank=True, choices=[('A', 'ARQUITECTO'), ('I', 'INGENIERO')], help_text='Profesión', max_length=1, verbose_name='Profesión')),
                ('mobile', models.CharField(blank=True, help_text='Número de Teléfono Celular', max_length=12, verbose_name='Celular')),
                ('phone', models.CharField(blank=True, help_text='Número de Teléfono Fijo o de Oficina', max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(default='correo@dominio.com', help_text='Correo Electrónico', max_length=50, verbose_name='Email')),
                ('tuition', models.PositiveIntegerField(blank=True, help_text='Colegiatura', null=True, verbose_name='Colegiatura')),
                ('secret_code', models.PositiveIntegerField(blank=True, help_text='Código Secreto de Arquitecto', null=True, verbose_name='Código Secreto de Arquitecto')),
                ('address', models.CharField(blank=True, help_text='Dirección', max_length=200, verbose_name='Dirección')),
                ('area_interest', models.CharField(blank=True, help_text='areas de interes', max_length=200, verbose_name='areas de interes')),
                ('institution', models.CharField(blank=True, help_text='Institucion', max_length=200, verbose_name='Institucion')),
                ('photo', models.ImageField(blank=True, help_text='Suba una fotografía en tamaño pasaporte o carnet', null=True, upload_to=apps.models.upload_photos, verbose_name='Fotografía')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('user', models.OneToOneField(blank=True, help_text='Usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Relacion de Miembros',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planame', models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Plan')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
            ],
            options={
                'verbose_name_plural': 'Planes de Suscripcion',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user_profile', models.OneToOneField(help_text='Usuario', on_delete=django.db.models.deletion.CASCADE, to='apps.member', verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.CreateModel(
            name='Policies_usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Titulo de Consulta', max_length=200, verbose_name='Titulo de Consulta')),
                ('message', models.TextField(help_text='Respuesta', verbose_name='Respuesta')),
                ('platform', models.CharField(choices=[('F', 'FORO'), ('N', 'NORMAS')], help_text='Plataforma', max_length=1, verbose_name='Plataforma')),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('norma_name', models.ManyToManyField(related_name='normas_rel', to='normas.Master_Normas')),
            ],
            options={
                'verbose_name_plural': 'Preguntas Frecuentes',
            },
        ),
        migrations.CreateModel(
            name='Control_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(blank=True, choices=[('E', 'VISA'), ('V', 'EFECTIVO')], help_text='Metodo de Pago', max_length=1, verbose_name='Metodo de Pago')),
                ('pay_import', models.DecimalField(decimal_places=2, help_text='Importe Pagado', max_digits=10, verbose_name='Importe Pagado')),
                ('validity_date_start', models.DateField(help_text='Fecha', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('id_plan', models.OneToOneField(blank=True, help_text='Plan Suscrito', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.plan', verbose_name='Plan de Suscripcion')),
                ('member', models.OneToOneField(blank=True, help_text='Miembros', null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.member', verbose_name='Miembros')),
            ],
            options={
                'verbose_name_plural': 'Control de Pagos',
            },
        ),
    ]
