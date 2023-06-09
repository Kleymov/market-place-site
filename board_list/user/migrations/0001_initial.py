# Generated by Django 4.1.5 on 2023-03-20 15:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Отображаемое имя')),
                ('last_name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
