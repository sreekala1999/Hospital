# Generated by Django 4.2.4 on 2023-09-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='doctor_image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='doctors',
            name='specialize',
            field=models.CharField(max_length=200),
        ),
    ]
