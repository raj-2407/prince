# Generated by Django 3.2.5 on 2021-11-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(default=0, max_length=5),
        ),
    ]
