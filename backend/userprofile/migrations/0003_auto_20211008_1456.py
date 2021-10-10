# Generated by Django 3.2.8 on 2021-10-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20211008_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='latitude',
            field=models.CharField(default=30.5, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='longitude',
            field=models.CharField(default=80, max_length=200),
            preserve_default=False,
        ),
    ]