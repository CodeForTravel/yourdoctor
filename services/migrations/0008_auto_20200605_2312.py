# Generated by Django 3.0.2 on 2020-06-05 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20200605_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='approved',
            new_name='is_approved',
        ),
    ]
