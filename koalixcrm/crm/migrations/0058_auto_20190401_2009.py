# Generated by Django 2.1.5 on 2019-04-01 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0057_merge_20190106_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='offersShipmentToCustomers',
            new_name='offers_shipment_to_customers',
        ),
    ]