# Generated by Django 4.2.7 on 2023-11-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_alter_book_ebook_alter_book_number_of_copies_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="number_of_copies_available",
            field=models.PositiveIntegerField(default=0),
        ),
    ]