# Generated by Django 3.0.2 on 2020-06-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0030_auto_20200616_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='73ab51', max_length=20, unique=True),
        ),
    ]
