# Generated by Django 5.1.1 on 2024-09-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='country',
            field=models.BooleanField(default=False),
        ),
    ]
