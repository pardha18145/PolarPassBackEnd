# Generated by Django 5.0.6 on 2024-07-23 20:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_orderitems_product"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderItems",
            new_name="OrderItem",
        ),
    ]
