# Generated by Django 3.2.15 on 2023-06-05 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230605_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera_image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]