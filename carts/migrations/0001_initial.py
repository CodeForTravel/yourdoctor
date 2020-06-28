# Generated by Django 3.0.2 on 2020-06-26 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('appointment_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(blank=True, max_length=50, null=True)),
                ('appointment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('appointment_fee', models.DecimalField(decimal_places=2, default='00.00', max_digits=10)),
                ('appointment_complete', models.BooleanField(default=False)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='30d7bd', max_length=20, unique=True)),
                ('status', models.CharField(choices=[('pending_payment', 'Pending Payment'), ('processing', 'Processing'), ('refund_initiated', 'Refund Initiated'), ('refunded', 'Refunded')], default='pending_payment', max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('carts', models.ManyToManyField(to='carts.CartItem')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('Bkash', 'Bkash'), ('Nagad', 'Nagad'), ('Rocket', 'Rocket')], default='Bkash', max_length=100)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete'), ('failed', 'Failed')], default='pending', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='carts.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='carts.Payment'),
        ),
    ]
