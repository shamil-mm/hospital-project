# Generated by Django 4.1.2 on 2022-11-08 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='dep_discription',
            new_name='dep_description',
        ),
        migrations.RemoveField(
            model_name='doctors',
            name='dep_name',
        ),
        migrations.AddField(
            model_name='doctors',
            name='department_description',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='d_description', to='hospitalapp.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctors',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='d_name', to='hospitalapp.department'),
            preserve_default=False,
        ),
    ]
