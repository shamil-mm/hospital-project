# Generated by Django 4.1.2 on 2022-11-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0008_rename_department_description_doctors_dep_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
