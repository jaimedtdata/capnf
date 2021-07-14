# Generated by Django 3.2 on 2021-07-13 21:21

import apps.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20210713_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories_normas',
            name='validity_date_finish',
        ),
        migrations.RemoveField(
            model_name='categories_normas',
            name='validity_date_start',
        ),
        migrations.RemoveField(
            model_name='location_normas',
            name='validity_date_finish',
        ),
        migrations.RemoveField(
            model_name='location_normas',
            name='validity_date_start',
        ),
        migrations.RemoveField(
            model_name='subcategories_normas',
            name='validity_date_finish',
        ),
        migrations.RemoveField(
            model_name='subcategories_normas',
            name='validity_date_start',
        ),
        migrations.AlterField(
            model_name='categories_normas',
            name='category_name',
            field=models.CharField(help_text='Nombre de Plan', max_length=200, verbose_name='Nombre de la Categoria'),
        ),
        migrations.AlterField(
            model_name='master_normas',
            name='file',
            field=models.FileField(help_text='Suba el archivo o base legal', upload_to=apps.models.upload_signature, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='master_normas',
            name='subcategory_name',
            field=models.ForeignKey(help_text='registro de SubCategoria', on_delete=django.db.models.deletion.CASCADE, to='apps.subcategories_normas', verbose_name='SubCategoria'),
        ),
    ]