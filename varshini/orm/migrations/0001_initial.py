# Generated by Django 5.1.2 on 2024-11-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=30)),
                ('loan_amount', models.FloatField()),
                ('cust_acntno', models.IntegerField()),
                ('cust_name', models.CharField(max_length=50)),
            ],
        ),
    ]
