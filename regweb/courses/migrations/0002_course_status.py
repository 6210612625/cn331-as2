# Generated by Django 3.2.7 on 2021-09-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
