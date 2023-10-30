# Generated by Django 4.2.6 on 2023-10-27 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_generalslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='VendorSlider Image')),
            ],
            options={
                'verbose_name': 'VendorSlider',
                'verbose_name_plural': 'VendorSlider',
            },
        ),
    ]
