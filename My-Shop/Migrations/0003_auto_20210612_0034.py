# Generated by Django 3.2.3 on 2021-06-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myshop', '0002_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.CharField(max_length=10000),
        ),
    ]
