# Generated by Django 5.1.3 on 2024-12-02 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_loan_loan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='library.reader'),
        ),
    ]