# Generated by Django 4.2.7 on 2024-01-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='Введите ник:', max_length=50)),
                ('password', models.TextField(blank=True, help_text='Введите пароль:', null=True)),
            ],
        ),
    ]
