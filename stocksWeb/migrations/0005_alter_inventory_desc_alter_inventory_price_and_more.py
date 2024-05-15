# Generated by Django 5.0.3 on 2024-05-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksWeb', '0004_remove_inventory_id_inventory_desc_inventory_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='productId',
            field=models.AutoField(max_length=60, primary_key=True, serialize=False),
        ),
    ]
