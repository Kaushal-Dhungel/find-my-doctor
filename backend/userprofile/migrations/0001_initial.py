# Generated by Django 3.2.8 on 2021-10-07 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userprofile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('identity', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('LGBTQ+', 'LGBTQ+')], max_length=30)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('avatar', models.ImageField(default='media/avatars/avatar.png', upload_to='avatars/')),
                ('facebook_link', models.CharField(blank=True, max_length=200)),
                ('twitter_link', models.CharField(blank=True, max_length=200)),
                ('instagram_link', models.CharField(blank=True, max_length=200)),
                ('clinic_name', models.CharField(blank=True, max_length=200)),
                ('ethnicity', models.CharField(blank=True, choices=[('Asian', 'Asian'), ('South Asian', 'South Asian'), ('Black', 'Black'), ('American Biracial', 'American Biracial'), ('White', 'White'), ('Jew', 'Jew'), ('Arab', 'Arab')], max_length=30)),
                ('education', models.CharField(blank=True, max_length=400)),
                ('religion', models.CharField(blank=True, max_length=200)),
                ('native_country', models.CharField(blank=True, max_length=200)),
                ('fav_sport', models.CharField(blank=True, max_length=200)),
                ('fav_team', models.CharField(blank=True, max_length=200)),
                ('fav_movie', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=userprofile.models.Image.generate_filename)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='userprofile.profile')),
            ],
        ),
    ]
