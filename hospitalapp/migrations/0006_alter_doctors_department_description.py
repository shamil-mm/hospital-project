# Generated by Django 4.1.2 on 2022-11-08 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0005_alter_doctors_department_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='department_description',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, related_name='d_description', to='hospitalapp.department'),
        ),
    ]
