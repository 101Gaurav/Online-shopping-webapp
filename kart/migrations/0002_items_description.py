# Generated by Django 3.0.4 on 2020-04-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
