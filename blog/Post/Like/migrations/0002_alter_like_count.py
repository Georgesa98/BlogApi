# Generated by Django 5.0.4 on 2024-05-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Like', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
