# Generated by Django 3.2 on 2021-08-16 10:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
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
    ]