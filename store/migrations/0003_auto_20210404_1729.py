# Generated by Django 3.1.7 on 2021-04-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quanwtity',
            new_name='quantity',
        ),
    ]
