# Generated by Django 4.2.1 on 2023-06-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_camera_image_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hashed_password',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]
