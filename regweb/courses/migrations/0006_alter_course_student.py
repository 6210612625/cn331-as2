# Generated by Django 3.2.7 on 2021-09-18 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_auto_20210917_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
