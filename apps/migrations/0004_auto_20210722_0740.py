# Generated by Django 3.2 on 2021-07-22 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20210722_0731'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Area_interest',
        ),
        migrations.RemoveField(
            model_name='coments_foro',
            name='themas',
        ),
        migrations.RemoveField(
            model_name='coments_foro',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subcategories_foro',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='themas_foro',
            name='subcategories',
        ),
        migrations.DeleteModel(
            name='Categories_foro',
        ),
        migrations.DeleteModel(
            name='Coments_foro',
        ),
        migrations.DeleteModel(
            name='Subcategories_foro',
        ),
        migrations.DeleteModel(
            name='Themas_foro',
        ),
    ]