# Generated by Django 2.2 on 2020-11-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemsapp', '0004_auto_20201117_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingorder',
            name='billingorder_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='purchaseorder_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
