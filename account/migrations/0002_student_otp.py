# Generated by Django 4.0.3 on 2023-11-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
