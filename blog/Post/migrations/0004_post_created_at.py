# Generated by Django 5.0.4 on 2024-05-15 13:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]