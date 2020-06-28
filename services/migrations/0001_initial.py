# Generated by Django 3.0.2 on 2020-06-26 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('clinic_name', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('patient_per_day', models.IntegerField(default=0)),
                ('is_approved', models.BooleanField(default=False)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_appointment_fee', models.DecimalField(decimal_places=2, default='00.00', max_digits=20)),
                ('old_appointment_fee', models.DecimalField(decimal_places=2, default='00.00', max_digits=20)),
                ('report_appointment_fee', models.DecimalField(decimal_places=2, default='00.00', max_digits=20)),
                ('service', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
    ]
