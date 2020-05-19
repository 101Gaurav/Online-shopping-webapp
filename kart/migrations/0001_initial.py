# Generated by Django 3.0.4 on 2020-04-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='others', max_length=100)),
                ('name', models.CharField(default='abc', max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
