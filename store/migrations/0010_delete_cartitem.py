# Generated by Django 4.0.4 on 2022-05-12 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_uuid_cart_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]