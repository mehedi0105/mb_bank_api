# Generated by Django 5.0.7 on 2024-09-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_alter_transaction_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('deposit', 'deposit'), ('loan_paid', 'loan_paid'), ('loan', 'loan'), ('withdraw', 'withdraw'), ('transfer_money', 'transfer_money')], max_length=100),
        ),
    ]
