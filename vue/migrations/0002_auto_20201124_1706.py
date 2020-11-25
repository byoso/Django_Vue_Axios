# Generated by Django 3.1.3 on 2020-11-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poulet',
            name='nom',
            field=models.CharField(max_length=31, unique=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='poulet',
            name='poids',
            field=models.FloatField(verbose_name='poids'),
        ),
    ]
