# Generated by Django 4.1.3 on 2022-11-04 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID',default=1)),
                ('dr_name', models.CharField(max_length=255)),
                ('dr_spec', models.CharField(max_length=255)),
                ('dr_image', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.department')),
            ],
        ),
    ]
