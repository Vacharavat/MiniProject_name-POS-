# Generated by Django 3.0.4 on 2020-03-11 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0007_auto_20200311_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_products',
            name='product',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='POS.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Type',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='POS.Product_type'),
        ),
    ]
