# Generated by Django 4.1 on 2024-11-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_loan_chk_return_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', through='library.BookAuthor', to='library.author'),
        ),
    ]
