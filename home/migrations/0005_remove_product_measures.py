# Generated by Django 4.1.7 on 2023-03-20 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='measures',
        ),
    ]
