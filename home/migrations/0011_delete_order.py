# Generated by Django 3.2.5 on 2021-11-06 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_order_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
    ]
