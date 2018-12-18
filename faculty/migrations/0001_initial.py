# Generated by Django 2.1.4 on 2018-12-18 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyProfileInfo',
            fields=[
                ('fid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='faculty', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
