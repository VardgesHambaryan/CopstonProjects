# Generated by Django 4.2.6 on 2023-10-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_addchar_additionalinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalinformation',
            name='char',
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='char',
            field=models.ManyToManyField(to='main.addchar'),
        ),
    ]
