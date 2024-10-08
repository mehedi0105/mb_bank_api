# Generated by Django 5.0.7 on 2024-09-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_amount',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[(1, 'loan'), (3, 'deposit'), (4, 'withdraw'), (2, 'Loan Paid'), (5, 'transfer_money')], max_length=100),
        ),
    ]
