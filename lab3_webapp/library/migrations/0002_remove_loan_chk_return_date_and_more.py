# Generated by Django 4.1 on 2024-11-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='loan',
            name='chk_return_date',
        ),
        migrations.AddConstraint(
            model_name='loan',
            constraint=models.CheckConstraint(check=models.Q(('return_date__isnull', True), ('return_date__gte', models.F('loan_date')), _connector='OR'), name='chk_loan_return_date'),
        ),
    ]
