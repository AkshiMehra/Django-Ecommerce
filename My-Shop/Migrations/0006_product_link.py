# Generated by Django 3.2.3 on 2021-06-15 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myshop', '0005_product_instock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(default='Link', max_length=100),
        ),
    ]
