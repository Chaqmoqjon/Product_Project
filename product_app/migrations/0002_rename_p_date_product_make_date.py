# Generated by Django 5.0.3 on 2024-03-06 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_date',
            new_name='make_date',
        ),
    ]
