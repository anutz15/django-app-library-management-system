# Generated by Django 4.2.7 on 2023-11-09 06:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("issuebook", "0002_issuedbooks_bookid_alter_issuedbooks_date_of_issue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issuedbooks",
            name="date_of_submission",
            field=models.DateField(default=datetime.date(2023, 11, 9)),
        ),
    ]
