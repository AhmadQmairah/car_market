# Generated by Django 2.1.5 on 2019-08-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_car_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]