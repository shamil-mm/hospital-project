# Generated by Django 4.1.2 on 2022-11-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0011_doctors_booking_dr_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
