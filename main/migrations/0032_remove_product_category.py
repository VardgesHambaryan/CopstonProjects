# Generated by Django 4.2.6 on 2023-10-30 15:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0031_alter_product_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
    ]
