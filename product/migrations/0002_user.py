# Generated by Django 4.1.5 on 2023-02-01 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('username', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Trường này chỉ dùng cho kiểu số.', regex='\\d*')])),
            ],
        ),
    ]
